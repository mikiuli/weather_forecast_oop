from typing import Protocol
from enum import Enum


class LogStorage(Protocol):
    def save(log: str):
        raise NotImplementedError


class LogFileStorage(LogStorage):
    def save(self, log: str):
        with open(file="log_storage.txt", mode="a", encoding="utf-8") as file:
            file.write(log)


class AvailableLogStorage(Enum):
    text_file_storage = LogFileStorage


def get_log_storage() -> LogStorage:
    return AvailableLogStorage.text_file_storage.value()
