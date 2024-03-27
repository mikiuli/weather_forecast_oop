"""Реализует хранилища для логов и выбор хранилища"""

from typing import Protocol


class LogStorage(Protocol):
    def save(self, log: str) -> None:
        """
        Сохраняет лог
        Params: log - лог
        Returns: -
        """
        raise NotImplementedError

    def clear(self) -> None:
        """
        Удаляет логи из хранилища
        Params: log - лог
        Returns: -
        """
        raise NotImplementedError


class FileLogStorage(LogStorage):
    def save(self, log: str):
        """
        Сохраняет лог в текстовом файле
        Params: log - лог
        Returns: -
        """
        with open(file="log_storage.txt", mode="a", encoding="utf-8") as file:
            file.write(log)

    def clear(self) -> None:
        """
        Удаляет логи из хранилища
        Params: -
        Returns: -
        """
        file = open(file="log_storage.txt", mode="w", encoding="utf-8")
        file.close()
