"""Интерфейс класса для получения прогноза погоды"""

from typing import Protocol

from models.weather import Weather


class WeatherGetter(Protocol):
    """Интерфейс класса для получения погоды по назанию города"""
    def get_weather_by_city(self, city: str) -> Weather:
        """
        Получает погоду по названию города
        Params: city - название города
        Returns: погоду в виде экземпляра класса Weather
        """
        raise NotImplementedError
