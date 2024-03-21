"""Реализует хранилища для логов и выбор хранилища"""

from typing import Protocol
from enum import Enum


class LogStorage(Protocol):
    def save(log: str) -> None:
        """
        Сохраняет лог
        Params: log - лог
        Returns: -
        """
        raise NotImplementedError


class LogFileStorage(LogStorage):
    def save(self, log: str):
        """
        Сохраняет лог в текстовом файле
        Params: log - лог
        Returns: -
        """
        with open(file="log_storage.txt", mode="a", encoding="utf-8") as file:
            file.write(log)


class AvailableLogStorage(Enum):
    """Доступные классы, в которых реализовано хранение логов"""
    text_file_storage = LogFileStorage


def get_log_storage() -> LogStorage:
    """
    Задаёт класс для хранения логов и возвращает экземпляр этого класса
    Params: -
    Returns: LogStorage
    """
    return AvailableLogStorage.text_file_storage.value()
