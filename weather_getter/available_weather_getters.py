"""Доступные сервисы получения погоды"""

from enum import Enum

from weather_getter.openweathermap_service import OpenWeatherapiService


class AvailableWeatherGetter(Enum):
    openweatherAPI = OpenWeatherapiService
