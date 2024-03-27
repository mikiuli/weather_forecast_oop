"""Реализует типы логов, их контент и сохранение в хранилище"""

from enum import Enum
import datetime
import traceback
import dataclasses

from ..logs_storages.logs_storages import LogStorage, FileLogStorage


class LogType(Enum):
    """Типы логов, которые отслеживаются"""
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclasses.dataclass
class LogContent:
    """Из чего состоит лог и как выглядит"""
    log_type: LogType
    module: str
    msg: str
    traceback: str = ''
    cur_time: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.now)

    def __str__(self) -> None:
        result = f"Тип лога: {self.log_type}, Время: {self.cur_time}, Модуль: {self.module}, Сообщение: {self.msg}"
        if self.traceback:
            result += f", traceback {self.traceback}"
        return f"{result}\n"


class Loger:
    """Логер: добавляет лог в хранилище"""
    def __init__(self, storage: LogStorage = FileLogStorage()) -> None:
        self._storage = storage

    def clear_storage(self) -> None:
        self._storage.clear()

    def error(self, module: str, msg: str, with_tb: bool = False) -> None:
        self._add_log(LogType.ERROR, module, msg, with_tb)

    def info(self, module: str, msg: str, with_tb: bool = False) -> None:
        self._add_log(LogType.INFO, module, msg, with_tb)

    def critical(self, module: str, msg: str, with_tb: bool = False) -> None:
        self._add_log(LogType.CRITICAL, module, msg, with_tb)

    def warning(self, module: str, msg: str, with_tb: bool = False) -> None:
        self._add_log(LogType.WARNING, module, msg, with_tb)

    def _add_log(self, log_type: LogType, module: str, msg: str, with_tb: bool = False) -> None:
        params = {
            "log_type": log_type,
            "module": module,
            "msg": msg,
        }
        if with_tb:
            params["traceback"] = traceback.format_exc()

        self._storage.save(str(LogContent(**params)))
