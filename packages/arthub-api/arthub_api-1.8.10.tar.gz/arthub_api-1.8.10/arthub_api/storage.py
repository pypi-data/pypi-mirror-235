"""
arthub_api.storage
~~~~~~~~~~~~~~

This module provides the operation interface of the ArtHub asset storage module
To visit the page of the asset storage module: "https://arthub.qq.com/trial/pan?node=304942678017"
"""
from . import utils
from . import models
from .utils import logger
import os
from xml.etree import ElementTree
from multiprocessing.pool import ThreadPool
import threading


class _TransferTaskScheduler(object):
    def __init__(self, thread_count=4, completed_cb=None):
        self._completed_cb = completed_cb
        self._completed = 0
        self._thread_p = ThreadPool(thread_count)
        self._async_tasks = []
        self._lck = threading.Lock()

    @staticmethod
    def _execute_task(task, task_scheduler):
        new_tasks = []
        res = task.process(new_tasks)
        for new_task in new_tasks:
            task_scheduler.schedule_task(new_task)
        return res

    def schedule_task(self, task):
        with self._lck:
            self._async_tasks.append(
                self._thread_p.apply_async(
                    func=_TransferTaskScheduler._execute_task,
                    args=[task, self]
                )
            )

    def pop_async_task(self):
        with self._lck:
            if len(self._async_tasks) == 0:
                return None
            return self._async_tasks.pop(0)

    def _terminate_sync(self):
        with self._lck:
            self._thread_p.terminate()
            self._thread_p.join()

    def join(self):
        return_data_list = []
        while True:
            async_ = self.pop_async_task()
            if async_ is None:
                # all async tasks have returned
                break
            res = async_.get()
            if not res.is_succeeded():
                # When a task fails, terminate all tasks
                self._terminate_sync()
                return res

            # When a task success
            # progress
            if (res.progress_weight is not None) and (res.progress_weight > 0) and (self._completed_cb is not None):
                self._completed += res.progress_weight
                self._completed_cb(self._completed)

            # Add to return data list
            return_data_list.append(res.data)
        return models.success_result(return_data_list)


def _execute_transfer_tasks_concurrently(task, completed_cb=None):
    scheduler = _TransferTaskScheduler(completed_cb=completed_cb)
    scheduler.schedule_task(task)
    return scheduler.join()


class _DownloadTask(object):
    def __init__(self, storage, asset_hub, remote_node, local_dir_path, download_filters, same_name_override,
                 download_temporary_dir_path=None):
        self._remote_node = remote_node
        self._local_dir_path = local_dir_path
        self._storage = storage
        self._asset_hub = asset_hub
        self._download_filters = download_filters
        self._same_name_override = same_name_override
        self._download_temporary_dir_path = download_temporary_dir_path

    def download_file(self, local_node_path):
        # get download signature url
        node_id = self._remote_node["id"]
        api_res = self._storage.open_api.depot_get_download_signature(self._asset_hub, [{
            "object_id": node_id,
            "object_meta": "origin_url"
        }])
        if not api_res.is_succeeded():
            return models.failure_result("get download signature of %d failed, %s" % (
                node_id, api_res.error_message()))
        signed_url = api_res.direct_result

        download_dir_path = os.path.dirname(local_node_path)
        if self._download_temporary_dir_path is not None:
            download_temp_dir_path = self._download_temporary_dir_path
        else:
            download_temp_dir_path = download_dir_path

        if not utils.mkdir(download_temp_dir_path):
            return models.failure_result("create download temp directory \"%s\" failed" % download_temp_dir_path)

        file_name = os.path.basename(local_node_path)
        download_temp_file_path = os.path.join(download_temp_dir_path, os.path.splitext(file_name)[0])
        download_temp_file_path += utils.get_random_string(2)
        download_temp_file_path += ".adl"
        download_temp_file_path = utils.rename_path_text(download_temp_file_path)

        # download file to disks
        res = utils.download_file(signed_url, download_temp_file_path)
        if not res.is_succeeded():
            return models.failure_result("download file failed, %s" % res.error_message())

        if not utils.mkdir(os.path.dirname(download_dir_path)):
            return models.failure_result("create download directory \"%s\" failed" % download_dir_path)

        if not utils.rename_path(download_temp_file_path, local_node_path):
            utils.remove(download_temp_file_path)
            return models.failure_result(
                "rename download temporary file \"%s\" to \"%s\" failed" % (download_temp_file_path, local_node_path))

        return models.success_result(None)

    def process(self, new_tasks_list):
        node_name = Storage.node_full_name(self._remote_node)
        node_path = os.path.join(self._local_dir_path, node_name)
        progress_weight = 0

        if not self._same_name_override:
            node_path = utils.rename_path_text(node_path)

        if Storage.is_node_directory(self._remote_node):
            # create directory
            if not utils.mkdir(node_path):
                return models.failure_result("create local directory \"%s\" failed" % node_path)

            # process next level
            res = self._storage.get_child_nodes_brief(self._asset_hub, self._remote_node, self._download_filters)
            if not res.is_succeeded():
                return res
            for child_node in res.data:
                new_tasks_list.append(
                    _DownloadTask(self._storage, self._asset_hub, child_node, node_path, self._download_filters,
                                  self._same_name_override))

        elif Storage.is_node_file(self._remote_node):
            res = self.download_file(node_path)
            if not res.is_succeeded():
                return res
            progress_weight = 1

        return models.success_task_result(node_path, progress_weight)


class _UploadTask(object):
    def __init__(self, storage, asset_hub, remote_parent_dir_id, local_path, same_name_override,
                 need_convert, tags_to_create, description):
        self._storage = storage
        self._asset_hub = asset_hub
        self._remote_parent_dir_id = remote_parent_dir_id
        self._local_path = local_path
        self._same_name_override = same_name_override
        self._need_convert = need_convert
        self._tags_to_create = tags_to_create
        self._remote_node_name = os.path.basename(self._local_path)
        self._asset_id = -1
        self._origin_url = -1
        self._upload_id = -1
        self._description = description

    class UploadChunk(object):
        def __init__(self, part_num, offset, length):
            self.part_num = part_num
            self.offset = offset
            self.length = length
            self.etag = ""

    def upload_chunk(self, chunk):
        # get signature url
        res = self._storage.open_api.depot_get_part_upload_signature(self._asset_hub, [{
            "object_id": self._asset_id,
            "object_meta": "origin_url",
            "file_name": self._remote_node_name,
            "upload_id": self._upload_id,
            "origin_url": self._origin_url,
            "part_number": chunk.part_num
        }])
        if not res.is_succeeded():
            return models.failure_result("get \"%d\"th part upload url failed, %s" % (
                chunk.part_num, res.error_message()))
        upload_url = res.direct_result
        logger.info("get multipart upload url: %s" % upload_url)

        # upload
        res = utils.upload_part_of_file(upload_url, self._local_path, chunk.offset, chunk.length)
        if not res.is_succeeded():
            return models.failure_result("upload \"%d\"th part failed, %s" % (
                chunk.part_num, res.error_message()))

        chunk.etag = res.data.headers.get("etag").strip('"')
        return models.success_result(None)

    @staticmethod
    def generate_etags_xml(chunks):
        root = ElementTree.Element('CompleteMultipartUpload')
        for chunk in chunks:
            part = ElementTree.SubElement(root, 'Part')
            etag = ElementTree.SubElement(part, 'ETag')
            etag.text = chunk.etag
            part_number = ElementTree.SubElement(part, 'PartNumber')
            part_number.text = str(chunk.part_num)
        return ElementTree.tostring(root)

    def _create_empty_file_on_storage(self):
        res = self._storage.open_api.depot_create_empty_file(self._asset_hub, self._asset_id, self._remote_node_name)
        if not res.is_succeeded():
            return res
        self._origin_url = res.data["origin_url"]
        return models.success_result(None)

    def _upload_to_storage(self):
        file_total_size = os.path.getsize(self._local_path)
        if file_total_size == 0:
            # create empty file
            return self._create_empty_file_on_storage()

        # create multipart upload task
        res = self._storage.open_api.depot_get_multipart_upload_id(self._asset_hub, self._asset_id,
                                                                   self._remote_node_name)
        if not res.is_succeeded():
            return res
        self._upload_id = res.data["upload_id"]
        self._origin_url = res.data["origin_url"]

        # allocate into chunks
        chunk_capacity = 32 * 1024 * 1024
        upload_chunks = []
        offset = 0
        part_num = 1
        while offset != file_total_size:
            next_offset = min(offset + chunk_capacity, file_total_size)
            upload_chunks.append(self.UploadChunk(part_num, offset, next_offset - offset))
            part_num += 1
            offset = next_offset

        # upload chunks serially
        for chunk in upload_chunks:
            res = self.upload_chunk(chunk)
            if not res.is_succeeded():
                return res
        etags_xml = self.generate_etags_xml(upload_chunks)

        # merge chunks
        res = self._storage.open_api.depot_complete_multipart_upload(self._asset_hub, self._asset_id,
                                                                     self._remote_node_name,
                                                                     self._upload_id,
                                                                     self._origin_url,
                                                                     etags_xml)
        if not res.is_succeeded():
            return res
        return models.success_result(None)

    def _upload_file(self):
        # create asset
        api_res = self._storage.open_api.depot_create_asset(self._asset_hub, [{
            "parent_id": self._remote_parent_dir_id,
            "name": self._remote_node_name,
            "add_new_version": self._same_name_override,
            "description": self._description
        }])
        if not api_res.is_succeeded():
            return models.failure_result("create asset in %d failed, %s" % (
                self._remote_parent_dir_id, api_res.error_message()))
        self._asset_id = api_res.direct_result

        # upload file to S3 storage
        res = self._upload_to_storage()
        if not res.is_succeeded():
            return res

        # update asset
        api_res = self._storage.open_api.depot_update_asset_by_id(self._asset_hub, [{
            "id": self._asset_id,
            "origin_url": self._origin_url
        }])
        if not api_res.is_succeeded():
            return models.failure_result("update asset %d failed, %s" % (
                self._asset_id, api_res.error_message()))

        # convert asset
        if self._need_convert:
            api_res = self._storage.open_api.depot_convert_asset(self._asset_hub, asset_files=[self._origin_url],
                                                                 asset_ids=[self._asset_id])
            if not api_res.is_succeeded():
                return models.failure_result("convert asset %d failed, %s" % (
                    self._asset_id, api_res.error_message()))

        # add tags
        if self._tags_to_create:
            api_res = self._storage.open_api.depot_add_asset_tag(self._asset_hub, asset_id=self._asset_id,
                                                                 tag_name=self._tags_to_create)
            if not api_res.is_succeeded():
                return models.failure_result("add tags to asset %d failed, %s" % (
                    self._asset_id, api_res.error_message()))

        return models.success_result(self._asset_id)

    def process(self, new_tasks_list):
        uploaded_node_id = -1
        progress_weight = 0
        if os.path.isdir(self._local_path):
            # create directory
            res = self._storage.open_api.depot_create_directory(self._asset_hub, [{
                "parent_id": self._remote_parent_dir_id,
                "name": self._remote_node_name,
                "allowed_rename": True,
                "return_existing_id": self._same_name_override
            }])
            if not res.is_succeeded():
                return models.failure_result("create remote directory \"%s\" failed" % self._remote_node_name)
            uploaded_node_id = res.direct_result

            # process next level
            child_nodes = os.listdir(self._local_path)
            for name in child_nodes:
                child_path = os.path.join(self._local_path, name)
                new_tasks_list.append(
                    _UploadTask(self._storage, asset_hub=self._asset_hub,
                                remote_parent_dir_id=uploaded_node_id,
                                local_path=child_path,
                                tags_to_create=self._tags_to_create,
                                same_name_override=self._same_name_override,
                                need_convert=self._need_convert,
                                description=self._description))
        elif os.path.isfile(self._local_path):
            res = self._upload_file()
            if not res.is_succeeded():
                return res
            uploaded_node_id = res.data
            progress_weight = 1

        return models.success_task_result(uploaded_node_id, progress_weight)


class TreeNode(object):
    def __init__(self, brief, parent):
        self.brief = brief
        self.parent = parent
        self.children = []

    @property
    def is_directory(self):
        return Storage.is_node_directory(self.brief)

    @property
    def is_file(self):
        return Storage.is_node_file(self.brief)

    @property
    def fullname(self):
        return Storage.node_full_name(self.brief)

    @property
    def id(self):
        return self.brief["id"]


class Storage(object):
    def __init__(self, open_api):
        r"""Used to perform ArtHub storage operations, such as uploading and downloading files.

        :param open_api: class: arthub_api.API.
        """
        self.open_api = open_api

    @staticmethod
    def node_full_name(node):
        full_name = node.get("name")
        file_format = node.get("file_format")
        if file_format:
            full_name += '.'
            full_name += file_format
        return full_name

    @staticmethod
    def is_node_directory(node):
        return node.get("type") == "directory" or node.get("type") == "project"

    @staticmethod
    def is_node_file(node):
        return node.get("type") == "asset" or node.get("type") == "multiasset"

    @staticmethod
    def get_child_node_relative_path(child_node_brief, root_id):
        full_path_id = child_node_brief.get("full_path_id")
        full_path_name = child_node_brief.get("full_path_name")
        find_root = False
        root_pos = 0
        for i in range(len(full_path_id)):
            if full_path_id[i] == root_id:
                root_pos = i
                find_root = True
                break
        if (not find_root) or (root_pos >= len(full_path_name)):
            return models.failure_result("root id %d not found" % root_id)

        relative_paths = []
        for i in range(root_pos + 1, len(full_path_name)):
            relative_paths.append(full_path_name[i])

        relative_paths.append(Storage.node_full_name(child_node_brief))
        return models.success_result(relative_paths)

    def get_child_nodes_brief_by_id(self, asset_hub, parent_node_id, query_filters=[], is_recursive=False,
                                    simplified_meta=True):
        r"""Get child nodes brief under parent dir node by parent id.
        """
        res = self.open_api.depot_get_node_brief_by_ids(asset_hub, [parent_node_id], True)
        if not res.is_succeeded():
            return models.failure_result(
                "get parent node info by %d failed, %s" % (parent_node_id, res.error_message()))

        if not self.is_node_directory(res.first_result()):
            return models.failure_result("target parent node %d is not a directory" % parent_node_id)
        return self.get_child_nodes_brief(asset_hub, res.first_result(), query_filters, is_recursive, simplified_meta)

    def get_child_nodes_brief(self, asset_hub, parent_node, query_filters=[], is_recursive=False, simplified_meta=True):
        r"""Get child nodes brief under parent dir node.

        :param asset_hub: str. Example: "trial".
        :param parent_node: dic. dir type node brief.
        :param simplified_meta: (optional) bool. Just basic meta, lower bandwidth consumption.
        :param query_filters: (optional) list<query_filter (dict) >. Example: [{"meta": "type",
                                                                                "condition": "x != project"}].
                {
                    "meta": filters meta,
                    "condition": filters condition
                }
        :param is_recursive: (optional) bool, Whether to query recursively

        :rtype: arthub_api.Result
                arthub_api.Result.data: list<dict>. child nodes brief
        """

        if not self.is_node_directory(parent_node):
            return models.failure_result("node type error")
        parent_id = parent_node.get("id")

        # step1: get count of child node
        direct_child_count = parent_node.get("direct_child_count")
        if is_recursive or direct_child_count is None:
            r = self.open_api.depot_get_child_node_count(asset_hub, [parent_id],
                                                         query_filters=query_filters,
                                                         is_recursive=is_recursive)
            if not r.is_succeeded():
                return models.failure_result("get child node count of %d failed, %s" % (parent_id, r.error_message()))
            child_count = r.direct_result
        else:
            child_count = direct_child_count

        if child_count == 0:
            return models.success_result([])

        # step2: get ids of child node
        child_ids = []
        batch_count = 1000
        offset = 0
        while offset < child_count:
            next_offset = child_count if (offset + batch_count) > child_count else (offset + batch_count)
            r = self.open_api.depot_get_child_node_id_in_range(asset_hub, parent_id, offset,
                                                               next_offset - offset,
                                                               query_filters=query_filters,
                                                               is_recursive=is_recursive)
            if not r.is_succeeded():
                return models.failure_result("get child node ids of %d failed, %s" % (parent_id, r.error_message()))
            child_ids += r.direct_result
            offset = next_offset

        # step3: get brief of child node
        child_nodes = []
        batch_count = 300
        offset = 0
        while offset < child_count:
            next_offset = child_count if (offset + batch_count) > child_count else (offset + batch_count)
            r = self.open_api.depot_get_node_brief_by_ids(asset_hub, child_ids[offset:next_offset],
                                                          simplified_meta=simplified_meta)
            if not r.is_succeeded():
                return models.failure_result("get child node brief failed, %s" % r.error_message())
            child_nodes += list(r.results.values())
            offset = next_offset

        return models.success_result(child_nodes)

    def get_child_nodes(self, asset_hub, parent_path, query_filters=[], is_recursive=False, simplified_meta=True):
        r"""Get child nodes under parent path.

        :param asset_hub: str. Example: "trial".
        :param parent_path: str. remote node path to query info. Example: "sdk/1/2".
        :param simplified_meta: (optional) bool. Just basic meta, lower bandwidth consumption.
        :param query_filters: (optional) list<query_filter (dict) >. Example: [{"meta": "type",
                                                                                "condition": "x != project"}].
                {
                    "meta": filters meta,
                    "condition": filters condition
                }
        :param is_recursive: (optional) bool, Whether to query recursively

        :rtype: arthub_api.Result
                arthub_api.Result.data: TreeNode, node of parent
        """

        # query root directory node
        res = self.get_node_by_path(asset_hub=asset_hub,
                                    remote_node_path=parent_path,
                                    simplified_meta=simplified_meta)
        if not res.is_succeeded():
            return models.failure_result("query root directory failed, %s" % (res.error_message()))

        root_node = TreeNode(brief=res.data, parent=None)

        # query child node
        def _query_children(parent_node):
            if not parent_node.is_directory:
                return models.success_result(None)
            _res = self.get_child_nodes_brief(asset_hub=asset_hub,
                                              parent_node=parent_node.brief,
                                              query_filters=query_filters,
                                              is_recursive=False,
                                              simplified_meta=simplified_meta)
            if not _res.is_succeeded():
                return models.failure_result("query children nodes failed")
            for child_brief in _res.data:
                child_node = TreeNode(brief=child_brief, parent=parent_node)
                if is_recursive:
                    _res_2 = _query_children(child_node)
                    if not _res_2.is_succeeded():
                        return models.failure_result("query children nodes failed")
                parent_node.children.append(child_node)
            return models.success_result(None)

        _query_children(root_node)
        return models.success_result(root_node)

    def upload_origin_file(self, asset_hub, remote_node_id, local_file_path, object_meta):
        res = self.open_api.depot_get_upload_signature(asset_hub, [{
            "object_id": remote_node_id,
            "object_meta": object_meta,
            "file_name": os.path.basename(local_file_path)
        }])
        if not res.is_succeeded():
            return models.failure_result(
                "get upload signature of node %d failed, %s" % (remote_node_id, res.error_message()))
        signed_upload_url = res.direct_result
        origin_url = res.first_result()["origin_url"]

        res = utils.upload_file(signed_upload_url, local_file_path)
        if not res.is_succeeded():
            return models.failure_result(
                "upload failed, %s" % res.error_message())
        return models.success_result(origin_url)

    def get_download_progress_total(self, asset_hub, remote_node):
        if self.is_node_directory(remote_node):
            res = self.open_api.depot_get_node_brief_by_ids(asset_hub, [remote_node["id"]])
            if res.is_succeeded():
                total_leaf_count = res.first_result().get("total_leaf_count")
                if total_leaf_count is not None:
                    return total_leaf_count
        return 1

    def download_node(self, asset_hub, node, local_dir_path, download_filters, same_name_override,
                      download_temporary_dir_path=None, progress_cb=None):
        completed_cb = None
        if progress_cb is not None:
            # res = self.get_download_progress_total(asset_hub, node)
            total_count = self.get_download_progress_total(asset_hub, node)

            def _completed_cb(completed):
                progress_cb(completed, total_count)

            completed_cb = _completed_cb

        # serially
        task = _DownloadTask(self, asset_hub, node, local_dir_path, download_filters, same_name_override,
                             download_temporary_dir_path=download_temporary_dir_path)
        return _execute_transfer_tasks_concurrently(task, completed_cb)

    @staticmethod
    def get_upload_progress_total(local_path):
        if os.path.isdir(local_path):
            return utils.count_files(local_path)
        return 1

    def upload_node(self, asset_hub, remote_dir_id, local_path, same_name_override,
                    need_convert, tags_to_create, description, progress_cb=None):
        completed_cb = None
        if progress_cb is not None:
            total_count = self.get_upload_progress_total(local_path)

            def _completed_cb(completed):
                progress_cb(completed, total_count)

            completed_cb = _completed_cb

        # serially
        task = _UploadTask(self, asset_hub, remote_dir_id, local_path, same_name_override, need_convert, tags_to_create,
                           description)
        return _execute_transfer_tasks_concurrently(task, completed_cb)

    def get_node_by_path(self, asset_hub, remote_node_path, simplified_meta=False):
        r"""Get node info by path in depot.

        :param asset_hub: str. Example: "trial".
        :param remote_node_path: str. remote node path to query info. Example: "sdk/1/2".
        :param simplified_meta: (optional) bool. Just basic meta, lower bandwidth consumption.

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when query successful
                arthub_api.Result.is_succeeded(): False when query fail, or node doesn't exist
                arthub_api.Result.data: dic. info of dir
        """

        res = self.open_api.depot_get_root_id(asset_hub)
        if not res.is_succeeded():
            r_ = models.failure_result("get depot root id failed, %s" % res.error_message())
            r_.set_data({"not_exist": False})
            return r_
        root_id = res.first_result()
        res = self.open_api.depot_get_node_brief_by_path(asset_hub, root_id, remote_node_path,
                                                         simplified_meta=simplified_meta)
        if not res.is_succeeded():
            r_ = models.failure_result("get node info by \"%s\" failed, %s" % (
                remote_node_path, res.error_message()))
            r_.set_data({"not_exist": res.is_node_not_exist()})
            return r_
        return models.success_result(res.first_result())

    def download_by_id(self, asset_hub, remote_node_id, local_dir_path, download_filters=[], same_name_override=True,
                       download_temporary_dir_path=None, progress_cb=None):
        r"""Download asset or directory by id to local directory.

        :param asset_hub: str. Example: "trial".
        :param remote_node_id: int. Example: 110347249755230.
        :param local_dir_path: str. Download target directory path. Example: "D://".
        :param download_filters: (optional) list<query_filter (dict) >. Example: [{"meta": "file_format",
                                                                                "condition": "x != png"}].
                {
                    "meta": filters meta,
                    "condition": filters condition
                }
        :param same_name_override: (optional) bool. When a file with the same name exists in the target path,
                                                    add new version
        :param download_temporary_dir_path: (optional) str. Directory where the downloaded temporary files are stored,
                                                            if None, the stored in local_dir_path
        :param progress_cb: (optional) function. Progress callback, params: (completed<int>, total<int>), rtype: None

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the download successful
                arthub_api.Result.is_succeeded(): False when the download fail
                arthub_api.Result.data: list<string>. path of downloaded file and dir, the first element is root path
        """

        res = self.open_api.depot_get_node_brief_by_ids(asset_hub, [remote_node_id])
        if not res.is_succeeded():
            return models.failure_result("get node info by %d failed, %s" % (remote_node_id, res.error_message()))
        return self.download_node(asset_hub, res.first_result(), local_dir_path, download_filters, same_name_override,
                                  download_temporary_dir_path, progress_cb)

    def download_by_path(self, asset_hub, remote_node_path, local_dir_path, download_filters=[],
                         same_name_override=True, download_temporary_dir_path=None, progress_cb=None):
        r"""Download asset or directory by path to local directory.

        :param asset_hub: str. Example: "trial".
        :param remote_node_path: str. Example: "sdk_test/storage_test/jpg&png".
        :param local_dir_path: str. Download target directory path. Example: "D://".
        :param download_filters: (optional) list<query_filter (dict) >. Example: [{"meta": "file_format", "condition": "x != png"}].
                {
                    "meta": filters meta,
                    "condition": filters condition
                }
        :param same_name_override: (optional) bool. When a file with the same name exists in the target path, add new
                                                    version
        :param download_temporary_dir_path: (optional) str. Directory where the downloaded temporary files are stored,
                                                            if None, the stored in local_dir_path
        :param progress_cb: (optional) function. Progress callback, params: (completed<int>, total<int>), rtype: None

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the download successful
                arthub_api.Result.is_succeeded(): False when the download fail
                arthub_api.Result.data: list<string>. path of downloaded file and dir, the first element is the root path
        """

        res = self.get_node_by_path(asset_hub, remote_node_path)
        if not res.is_succeeded():
            return models.failure_result("get node \"%s\" info failed, %s" % (remote_node_path,
                                                                              res.error_message()))

        return self.download_node(asset_hub, res.data, local_dir_path, download_filters, same_name_override,
                                  download_temporary_dir_path, progress_cb)

    def upload_to_directory_by_id(self, asset_hub, remote_dir_id, local_path, same_name_override=True,
                                  need_convert=True, tags_to_create=None, description=None, progress_cb=None):
        r"""Upload file or directory remote directory, with remote directory id.

        :param asset_hub: str. Example: "trial".
        :param remote_dir_id: int. Example: 110347250886196.
        :param local_path: str. Example: "D:/test/python/1.mp4".
        :param same_name_override: (optional) bool. When a file with the same name exists in the target path, add new
                                                    version
        :param need_convert: (optional) bool. Convert asset after upload (Effective for specific formats, such as video,
                                              model)
        :param tags_to_create: (optional) str[]. Create tags after upload. Example: ["Christmas", "Gun"]
        :param description: (optional) str. Add asset description. Example: "Gun"
        :param progress_cb: (optional) function. Progress callback, params: (completed<int>, total<int>), rtype: None

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the upload successful
                arthub_api.Result.is_succeeded(): False when the upload fail
                arthub_api.Result.data: list<id>. id of uploaded file and dir, the first element is the root path
        """

        res = self.open_api.depot_get_node_brief_by_ids(asset_hub, [remote_dir_id], simplified_meta=True)
        if not res.is_succeeded():
            return models.failure_result("get node info by %d failed, %s" % (remote_dir_id, res.error_message()))

        if not self.is_node_directory(res.first_result()):
            return models.failure_result("target node %d is not a directory" % remote_dir_id)

        return self.upload_node(asset_hub, res.first_result()["id"], local_path, same_name_override, need_convert,
                                tags_to_create, description, progress_cb)

    def upload_to_directory_by_path(self, asset_hub, remote_dir_path, local_path, same_name_override=True,
                                    need_convert=True, tags_to_create=None, description=None, progress_cb=None):
        r"""Upload file or directory remote directory, with remote directory path.

        :param asset_hub: str. Example: "trial".
        :param remote_dir_path: str. Example: "sdk_test/1/2".
        :param local_path: str. Example: "D:/test/python/1.mp4".
        :param same_name_override: (optional) bool. When a file with the same name exists in the target path, add new
                                                    version
        :param need_convert: (optional) bool. Convert asset after upload (Effective for specific formats, such as video,
                                              model)
        :param tags_to_create: (optional) bool. Create tags after upload. Example: ["Christmas", "Gun"]
        :param description: (optional) str. Add asset description. Example: "Gun"
        :param progress_cb: (optional) function. Progress callback, params: (completed<int>, total<int>), rtype: None

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the upload successful
                arthub_api.Result.is_succeeded(): False when the upload fail
                arthub_api.Result.data: list<id>. id of uploaded file and dir, the first element is the root path
        """

        res = self.create_directory_by_path(asset_hub, remote_dir_path)
        if not res.is_succeeded():
            return res

        return self.upload_node(asset_hub, res.data, local_path, same_name_override, need_convert,
                                tags_to_create, description, progress_cb)

    def upload_icon_by_id(self, asset_hub, remote_node_id, local_icon_file_path):
        r"""Upload icon of remote directory or asset. with remote directory id.

        :param asset_hub: str. Example: "trial".
        :param remote_node_id: int. id of remote directory or asset. Example: 110347250886196.
        :param local_icon_file_path: str. Example: "D:/icon.png".

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the upload successful
                arthub_api.Result.is_succeeded(): False when the upload fail
        """

        # check target node
        res = self.open_api.depot_get_node_brief_by_ids(asset_hub, [remote_node_id], True)
        if not res.is_succeeded():
            return models.failure_result(
                "get node info by %d failed, %s" % (remote_node_id, res.error_message()))
        target_node = res.first_result()

        # upload file
        res = self.upload_origin_file(asset_hub, remote_node_id, local_icon_file_path, "icon_url")
        if not res.is_succeeded():
            return res
        origin_url = res.data

        # update node
        if target_node["type"] == "directory":
            res = self.open_api.depot_update_directory_by_id(asset_hub, [{
                "id": remote_node_id,
                "icon_url": origin_url
            }])
        elif target_node["type"] == "project":
            res = self.open_api.depot_update_project_by_id(asset_hub, [{
                "id": remote_node_id,
                "icon_url": origin_url
            }])
        elif target_node["type"] == "asset":
            res = self.open_api.depot_update_asset_by_id(asset_hub, [{
                "id": remote_node_id,
                "preview_url": origin_url
            }])
        elif target_node["type"] == "multiasset":
            res = self.open_api.depot_update_multi_asset_by_id(asset_hub, [{
                "id": remote_node_id,
                "preview_url": origin_url
            }])
        else:
            return models.failure_result(
                "target node type wrong, %s" % target_node["type"])
        if not res.is_succeeded():
            return models.failure_result(
                "update node info by %d failed, %s" % (remote_node_id, res.error_message()))

        return models.success_result(origin_url)

    def upload_icon_by_path(self, asset_hub, remote_node_path, local_icon_file_path):
        r"""Upload icon of remote directory or asset. with remote node path.

        :param asset_hub: str. Example: "trial".
        :param remote_node_path: int. path of remote directory or asset. Example: "sdk_test/1/2".
        :param local_icon_file_path: str. Example: "D:/icon.png".

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the upload successful
                arthub_api.Result.is_succeeded(): False when the upload fail
        """
        res = self.get_node_by_path(asset_hub, remote_node_path, True)
        if not res.is_succeeded():
            return res
        node_id = res.data["id"]
        return self.upload_icon_by_id(asset_hub, node_id, local_icon_file_path)

    def create_direct_child_directory(self, asset_hub, parent_id, name, is_project):
        # try to get exist path
        res = self.open_api.depot_get_node_brief_by_path(asset_hub, parent_id, name)
        if res.is_succeeded():
            exist_node = res.first_result()
            if Storage.is_node_directory(exist_node):
                return models.success_result(exist_node["id"])
            else:
                return models.failure_result(
                    "target path \"%s\" isn't a directory but a %s" % (name, exist_node["type"]))
        if not res.is_node_not_exist():
            return models.failure_result(
                "get path \"%s\" info failed, %s" % (name, res.error_message()))

        if is_project:
            # create project
            res = self.open_api.depot_create_project(asset_hub, name, parent_id)
        else:
            # create directory
            res = self.open_api.depot_create_directory(asset_hub, [{
                "parent_id": parent_id,
                "name": name,
                "allowed_rename": True,
                "return_existing_id": True
            }])

        if not res.is_succeeded():
            return models.failure_result("create directory \"%s\" under %d failed, %s" % (
                name, parent_id, res.error_message()))
        dir_id = res.direct_result
        return models.success_result(dir_id)

    def create_directory_by_path(self, asset_hub, remote_dir_path):
        r"""Create directory by path in depot.

        :param asset_hub: str. Example: "trial".
        :param remote_dir_path: str. remote dir path to create. Example: "sdk/1/2".

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when create successful or a dir with the same name already exists
                arthub_api.Result.is_succeeded(): False when create fail
                arthub_api.Result.data: int. id of dir
        """

        res = self.open_api.depot_get_root_id(asset_hub)
        if not res.is_succeeded():
            return models.failure_result("get depot root id failed, %s" % res.error_message())
        root_id = res.first_result()

        remote_dir_path = remote_dir_path.replace('\\', '/')
        dir_path_list = utils.splite_path(remote_dir_path)
        if len(dir_path_list) == 0:
            return root_id

        # try to get exist path
        res = self.open_api.depot_get_node_brief_by_path(asset_hub, root_id, remote_dir_path)
        if res.is_succeeded():
            exist_node = res.first_result()
            if Storage.is_node_directory(exist_node):
                return models.success_result(exist_node["id"])
            else:
                return models.failure_result(
                    "target path \"%s\" isn't a directory but a %s" % (remote_dir_path, exist_node["type"]))
        if not res.is_node_not_exist():
            return models.failure_result(
                "get path \"%s\" info failed, %s" % (remote_dir_path, res.error_message()))

        # create root directory (project) under depot
        project_name = dir_path_list[0]
        res = self.create_direct_child_directory(asset_hub, root_id, project_name, True)
        if not res.is_succeeded():
            return models.failure_result("create project \"%s\" failed, %s" % (project_name, res.error_message()))

        current_dir_id = res.data
        dir_path_list.pop(0)

        # create directory under project
        for name in dir_path_list:
            res = self.create_direct_child_directory(asset_hub, current_dir_id, name, False)
            if not res.is_succeeded():
                return models.failure_result("create directory \"%s\" under %d failed, %s" % (
                    name, current_dir_id, res.error_message()))
            current_dir_id = res.data

        return models.success_result(current_dir_id)

    def delete_node_by_path(self, asset_hub, remote_node_path):
        r"""Upload file or directory remote directory, with remote directory id.

        :param asset_hub: str. Example: "trial".
        :param remote_node_path: str. remote node path tp remove (dir or file). Example: "sdk_test/1/to_remove".

        :rtype: arthub_api.Result
                arthub_api.Result.is_succeeded(): True when the deletion successful or the node doesn't exist
                arthub_api.Result.is_succeeded(): False when the deletion fail
                arthub_api.Result.data: int. id of deleted node
        """

        res = self.get_node_by_path(asset_hub, remote_node_path, simplified_meta=True)
        if not res.is_succeeded():
            if res.data and res.data.get("not_exist"):
                return models.success_result(-1)
            return res

        node_id = res.data["id"]
        api_res = self.open_api.depot_delete_node_by_ids(asset_hub, [
            node_id
        ])
        if not api_res.is_succeeded():
            return models.failure_result("delete node %d failed, %s" % (
                node_id, api_res.error_message()))
        return models.success_result(node_id)
