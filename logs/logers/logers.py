from enum import Enum
import datetime
import traceback
import dataclasses

from ..logs_storages.logs_storages import LogStorage, get_log_storage


class LogType(Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclasses.dataclass
class LogContent:
    log_type: LogType
    module: str
    msg: str
    traceback: str = ''
    cur_time: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.now)

    def __str__(self):
        result = f"Тип лога: {self.log_type}, Время: {self.cur_time}, Модуль: {self.module}, Сообщение: {self.msg}"
        if self.traceback:
            result += f", traceback {self.traceback}"
        return f"{result}\n"


class Loger:
    def __init__(self, storage: LogStorage = get_log_storage()):
        self._storage = storage

    def error(self, module: str, msg: str, with_tb: bool = False):
        self._add_log(LogType.ERROR, module, msg, with_tb)

    def info(self, module: str, msg: str, with_tb: bool = False):
        self._add_log(LogType.INFO, module, msg, with_tb)

    def critical(self, module: str, msg: str, with_tb: bool = False):
        self._add_log(LogType.CRITICAL, module, msg, with_tb)

    def warning(self, module: str, msg: str, with_tb: bool = False):
        self._add_log(LogType.WARNING, module, msg, with_tb)

    def _add_log(self, log_type: LogType, module: str, msg: str, with_tb: bool = False):
        params = {
            "log_type": log_type,
            "module": module,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        self._storage.save(str(LogContent(**params)))
