"""Создание хранилища, сохранение, получение, удаление данных"""

from .storages import Storage, ListStorage, SQLiteStorage, TextFileStorage


def create_weather_storage() -> Storage:
    """
    Создаёт хранилище данных о погоде
    Params: -
    Returns: хранилище
    """
    weather_storage = _get_weather_storage("sqlite3")
    return weather_storage


def _get_weather_storage(name: str) -> Storage:
    """
    Создаёт экземпляр хранилища
    Params: название
    Returns: хранилище
    """
    storages = {
        "sqlite3": SQLiteStorage,
        "weather_storage.txt": TextFileStorage,
        "list": ListStorage,
    }
    return storages.get(name)()
