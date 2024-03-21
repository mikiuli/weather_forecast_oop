"""Фикстуры для создания разных экземпляров хранилищ"""

import pytest

from weather_storage.sqlite_storage import SQLiteStorage
from weather_storage.txt_file_storage import TextFileStorage
from weather_storage.list_storage import ListStorage
from configs.configs import get_test_storage_name


@pytest.fixture(scope="session")
def sqlite_storage():
    """
    Создаёт экземпляр базы данных sqlite3
    Params: -
    Returns: экземпляр базы данных sqlite3
    """
    with SQLiteStorage(db_name=get_test_storage_name()) as sqlite_storage:
        yield sqlite_storage


@pytest.fixture(scope="session")
def text_storage():
    """
    Создаёт экземпляр текстового хранилища данных
    Params: -
    Returns: экземпляр текстового хранилища данных
    """
    with TextFileStorage(file_name=get_test_storage_name()) as text_file_storage:
        yield text_file_storage


@pytest.fixture(scope="session")
def list_storage():
    """
    Создаёт экземпляр хранилища данных в виде списка
    Params: -
    Returns: экземпляр хранилища данных в виде списка
    """
    with ListStorage() as list_storage:
        yield list_storage
