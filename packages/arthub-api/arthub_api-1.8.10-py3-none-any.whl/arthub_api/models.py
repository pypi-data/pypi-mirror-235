"""
arthub_api.models
~~~~~~~~~~~~~~~

This module contains the primary objects.
"""


def failure_result(error_message):
    return Result(succeeded=False, error_message=error_message)


def success_result(data):
    return Result(succeeded=True, data=data)


class Result(object):
    def __init__(self, succeeded, error_message="", data=None):
        self._succeeded = succeeded
        self._error_message = error_message
        self._data = data

    def __bool__(self):
        return self.is_succeeded()

    def is_succeeded(self):
        return self._succeeded

    def error_message(self):
        return self._error_message

    @property
    def data(self):
        return self._data

    def set_data(self, data_):
        self._data = data_


class TaskResult(Result):
    def __init__(self, succeeded, error_message="", data=None, progress_weight=0):
        super(TaskResult, self).__init__(succeeded, error_message, data)
        self._progress_weight = progress_weight

    @property
    def progress_weight(self):
        return self._progress_weight


def success_task_result(data, progress_weight=0):
    return TaskResult(succeeded=True, data=data, progress_weight=progress_weight)
