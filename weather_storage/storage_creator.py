"""Создание хранилища, сохранение, получение, удаление данных"""

from .storages import Storage, ListStorage, SQLiteStorage, TextFileStorage


class StorageCreator:
    """Создаёт хранилище данных"""
    def __init__(self):
        self.storage_type = "sqlite3"
        self.storages = {
            "sqlite3": SQLiteStorage,
            "weather_storage.txt": TextFileStorage,
            "list": ListStorage,
        }

    def create_weather_storage(self) -> Storage:
        """
        Создаёт хранилище данных о погоде
        Params: -
        Returns: хранилище
        """
        weather_storage = self._get_weather_storage()
        return weather_storage

    def _get_weather_storage(self) -> Storage:
        """
        Создаёт экземпляр хранилища
        Params: -
        Returns: хранилище
        """
        return self.storages.get(self.storage_type)()
