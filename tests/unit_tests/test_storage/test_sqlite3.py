"""Тестирование SQLiteStorage"""

from tests.fixtures.storage_sample_creator import sqlite_storage
from tests.fixtures.weather_samples import weather_data_samples

__all__ = [sqlite_storage, weather_data_samples, ]

# pytest ./tests/unit_tests/test_storage/test_sqlite3.py


class TestSQLiteStorage:
    """Тестирование SQLiteStorage"""
    def setup_method(self):
        self.data_length = 3
        self.less_lenght_data = 2

    def test_add_and_get_data(self, sqlite_storage, weather_data_samples):
        for data in weather_data_samples:
            sqlite_storage.save_weather_data(data=data)
        assert sqlite_storage.get_weather_data(number=3) == list(reversed(weather_data_samples))

    def test_add_and_delete_data(self, sqlite_storage, weather_data_samples):
        for data in weather_data_samples:
            sqlite_storage.save_weather_data(data=data)
        sqlite_storage.delete_weather_data()
        assert sqlite_storage.get_weather_data(number=2) == []

    def test_get_less_data(self, sqlite_storage, weather_data_samples):
        for data in weather_data_samples:
            sqlite_storage.save_weather_data(data=data)
        assert sqlite_storage.get_weather_data(number=self.less_lenght_data
                                               ) == list(reversed(weather_data_samples))[:self.less_lenght_data]

    def test_get_zero_data(self, sqlite_storage, weather_data_samples):
        for data in weather_data_samples:
            sqlite_storage.save_weather_data(data=data)
        assert sqlite_storage.get_weather_data(number=0) == []
