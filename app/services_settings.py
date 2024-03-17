"""Выбор сервисов для работы приложения"""

from weather_storage.available_storages import AvailableStorage
from weather_getter.available_weather_getters import AvailableWeatherGetter
from current_city_searcher.available_city_searchers import AvailableCitySearcher


def get_city_searcher():
    return AvailableCitySearcher.ipinfo.value()


def get_weather_getter():
    return AvailableWeatherGetter.openweatherAPI.value()


def get_storage():
    return AvailableStorage.sqlite3.value()
