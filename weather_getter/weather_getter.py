"""Получение погоды по названию города"""

from .weather_api_services import WeatherGetter, OpenWeatherapiGetter
from models.weather import Weather


def get_weather(city_name: str) -> Weather:
    """
    Получает погоду
    Params: city_name - название города в виде строки
    Returns: погоду в виде класса Weather
    """
    weather_getter = _get_weather_getter("openweathermap.org")
    weather = weather_getter.get_weather_by_city(city_name)
    return weather


def _get_weather_getter(name: str) -> WeatherGetter:
    """
    Создаёт экземпляр класса для получения прогноза погоды
    Params: название
    Returns: экземпляр класса для получения прогноза погоды
    """
    weather_getters_by_name = {
        "openweathermap.org": OpenWeatherapiGetter,
    }
    return weather_getters_by_name.get(name)()
