"""Доступные хранилища"""

from enum import Enum

from weather_storage.list_storage import ListStorage
from weather_storage.sqlite_storage import SQLiteStorage
from weather_storage.txt_file_storage import TextFileStorage


class AvailableStorage(Enum):
    sqlite3 = SQLiteStorage
    txt_file_storage = TextFileStorage
    list_storage = ListStorage
