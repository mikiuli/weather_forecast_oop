"""Пример прогноза погоды в виде класса Weather"""

import pytest

from models.weather import Weather


@pytest.fixture(scope="function")
def weather_data_samples() -> list[Weather]:
    """
    Возвращает 3 примера прогноза погоды в виде класса Weather
    Params: -
    Returns: список из 3 экземпляров класса Weather
    """
    first_weather_data = Weather(current_time="2024-03-15 00:07:31+03:00",
                                 city="Санкт-Петербург",
                                 weather_type="облачно с прояснениями",
                                 temperature=5,
                                 temperature_feels_like=1,
                                 wind_speed=5)
    second_weather_data = Weather(current_time="2024-03-15 00:07:38+06:00",
                                  city="Новосибирск",
                                  weather_type="ясно",
                                  temperature=-10,
                                  temperature_feels_like=-15,
                                  wind_speed=2)
    third_weather_data = Weather(current_time="2024-03-16 18:33:59+03:00",
                                 city="Казань",
                                 weather_type="ясно",
                                 temperature=-5,
                                 temperature_feels_like=-9,
                                 wind_speed=3)
    return [first_weather_data, second_weather_data, third_weather_data]
