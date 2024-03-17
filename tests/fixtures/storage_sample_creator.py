import pytest

from weather_storage.sqlite_storage import SQLiteStorage
from weather_storage.txt_file_storage import TextFileStorage
from weather_storage.list_storage import ListStorage
from configs.configs import get_test_storage_name


@pytest.fixture(scope="session")
def sqlite_storage():
    with SQLiteStorage(db_name=get_test_storage_name()) as sqlite_storage:
        yield sqlite_storage


@pytest.fixture(scope="session")
def text_storage():
    with TextFileStorage(file_name=get_test_storage_name()) as text_file_storage:
        yield text_file_storage


@pytest.fixture(scope="session")
def list_storage():
    with ListStorage() as list_storage:
        yield list_storage
