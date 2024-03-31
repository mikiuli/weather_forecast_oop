"""Тестирование OpenWeatherapiService"""

import pytest

from models.weather import Weather
from weather_getter.openweathermap_service import OpenWeatherapiService
from errors.errors import WrongCityName


# pytest ./tests/unit_tests/test_weather_getters/test_openweathermap_service.py

class TestOpenWeatherapiService:
    """Тестирование OpenWeatherapiService"""
    def setup_method(self):
        self.weather_service = OpenWeatherapiService()

    def test_getting_weather(self):
        assert isinstance(self.weather_service.get_weather_by_city("Санкт-Петербург"), Weather)

    def test_wrong_city_name(self):
        with pytest.raises(WrongCityName):
            self.weather_service.get_weather_by_city("СнктПтрг")
