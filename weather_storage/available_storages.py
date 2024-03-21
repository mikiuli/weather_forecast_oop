"""Доступные хранилища данных о погоде"""

from enum import Enum

from weather_storage.list_storage import ListStorage
from weather_storage.sqlite_storage import SQLiteStorage
from weather_storage.txt_file_storage import TextFileStorage


class AvailableStorage(Enum):
    """Доступные хранилища данных о погоде"""
    sqlite3 = SQLiteStorage
    txt_file_storage = TextFileStorage
    list_storage = ListStorage
