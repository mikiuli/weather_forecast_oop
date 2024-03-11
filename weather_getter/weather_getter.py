"""Получение погоды по названию города"""

from .weather_api_services import WeatherDataReceivingService, OpenWeatherapiService
from models.weather import Weather


class WeatherGetter:
    def __init__(self):
        self.selected_service = "openweathermap.org"
        self.services_by_name = {
            "openweathermap.org": OpenWeatherapiService,
        }

    def get_weather(self, city_name: str) -> Weather:
        """
        Получает погоду
        Params: city_name - название города в виде строки
        Returns: погоду в виде класса Weather
        """
        weather_service = self._get_weather_getter()
        weather = weather_service.get_weather_by_city(city_name)
        return weather

    def _get_weather_getter(self) -> WeatherDataReceivingService:
        """
        Создаёт экземпляр класса для получения прогноза погоды
        Params: -
        Returns: экземпляр класса для получения прогноза погоды
        """
        return self.services_by_name.get(self.selected_service)()
