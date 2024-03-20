"""Получение погоды с сервиса openweathermap"""

import json
from json.decoder import JSONDecodeError
from http import HTTPStatus
from datetime import datetime, timezone, timedelta

import requests

from .contracts import WeatherDataReceivingService
from models.weather import Weather, Celsius, MetresPerSec
from errors import errors
from configs.configs import get_openweather_key
from logs.logers.logers import Loger


class OpenWeatherapiService(WeatherDataReceivingService):
    """Получение погоды с сервиса openweathermap"""
    def get_weather_by_city(self, city_name: str) -> Weather:
        """
        Получает погоду по названию города
        Params: city - название города
        Returns: погоду в виде экземпляра класса Weather
        """
        json_openweather_response = self._get_openweather_response(
            openweatherAPI_key=get_openweather_key(),
            city_name=city_name
        )
        weather = self._parse_openweather_response(json_openweather_response)
        return weather

    @staticmethod
    def _check_status_code_OK(status_code: requests.status_codes) -> bool:
        """
        Проверяет статус код, который присылает сервер
        params: status_code - код ответа сервера
        returns: булевое значение
        """
        if status_code == HTTPStatus.OK:
            Loger().info(module=__name__,
                         msg=f"Ответ сервера со статусом {HTTPStatus.OK}")
            return True
        if status_code == HTTPStatus.NOT_FOUND:
            Loger().info(module=__name__,
                         msg=f"Ответ сервера со статусом {HTTPStatus.NOT_FOUND}")
            raise errors.WrongCityName()
        if status_code == HTTPStatus.UNAUTHORIZED:
            raise errors.WrongAPIError()
        if status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            raise errors.APIServiceError()
        raise errors.UnspecifiedError()

    def _get_openweather_response(self, openweatherAPI_key: str, city_name: str) -> dict:
        """
        Получает ответ от сервера, райзит ошибку, если проблемы с соединением
        params: openweatherAPI - API-ключ от openweathermap.org,
        city_name - имя города, погоду в котором хочет получить пользователь
        returns: Возвращает тело полученного ответа в виде текста
        """
        url = ("https://api.openweathermap.org/data/2.5/weather?"
               f"appid={openweatherAPI_key}&"
               "units=metric&lang=ru")
        try:
            Loger().info(module=__name__,
                         msg=f"Получаю ответ от внешнего сервера {url}")
            response = requests.get(url=url, timeout=3, params={"q": city_name})
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            raise errors.InternetIsNotAvailable()
        if OpenWeatherapiService._check_status_code_OK(response.status_code):
            try:
                Loger().info(module=__name__,
                             msg="Преобразую ответ сервера в JSON")
                openweather_dict = json.loads(response.text)
            except JSONDecodeError as e:
                Loger().critical(module=__name__,
                                 msg=f"Не могу преобразовать ответ сервера в JSON из-за {e}")
                raise errors.APIServiceError()
            return openweather_dict

    def _parse_openweather_response(self, openweather_dict: dict) -> Weather:
        """
        Превращает словарь в класс Weather
        params: openweather_response - тело полученного ответа в виде текса
        returns: погоду в виде класса Weather
        """
        try:
            return Weather(
                current_time=self._fetch_current_time(openweather_dict),
                city=self._fetch_city_name(openweather_dict),
                weather_type=self._fetch_weather_type(openweather_dict),
                temperature=self._fetch_temperature(openweather_dict),
                temperature_feels_like=self._fetch_temp_feels_like(openweather_dict),
                wind_speed=self._fetch_wind_speed(openweather_dict)
            )
        except (KeyError, IndexError):
            raise errors.APIServiceError

    def _fetch_current_time(self, openweather_dict: dict) -> datetime:
        """
        Получает текущее время из словаря
        params: openweather_dict - словарь
        returns: время в datetime формате
        """
        Loger().info(module=__name__, msg="Получаю текущее время")
        date = openweather_dict["dt"]
        tzinfo = openweather_dict["timezone"]
        tz = timezone(timedelta(seconds=tzinfo))
        formatted_time = datetime.fromtimestamp(date, tz=tz)
        return formatted_time

    def _fetch_city_name(self, openweather_dict: dict) -> str:
        """
        Получает имя города
        params: openweather_dict - словарь
        returns: имя города
        """
        Loger().info(module=__name__, msg="Получаю название города")
        return openweather_dict["name"]

    def _fetch_temperature(self, openweather_dict: dict) -> Celsius:
        """
        Получает температуру
        params: openweather_dict - словарь
        returns: температуру в цельсиях
        """
        Loger().info(module=__name__, msg="Получаю температуру")
        return round(openweather_dict["main"]["temp"])

    def _fetch_temp_feels_like(self, openweather_dict) -> Celsius:
        """
        Получает температуру "ощущается как"
        params: openweather_dict - словарь
        returns: температуру "ощущается как"
        """
        Loger().info(module=__name__, msg="Получаю температуру \"ощущается как\"")
        return round(openweather_dict["main"]["feels_like"])

    def _fetch_wind_speed(self, openweather_dict: dict) -> MetresPerSec:
        """
        Получает скорость ветра
        params: openweather_dict - словарь
        returns: скорость ветра
        """
        Loger().info(module=__name__, msg="Получаю скорость ветра")
        return round(openweather_dict["wind"]["speed"])

    def _fetch_weather_type(self, openweather_dict: dict) -> str:
        """
        Получает описание погоды
        params: openweather_dict - словарь
        returns: один из объектов класса WatherType
        """
        Loger().info(module=__name__, msg="Получаю описание погоды")
        return str(openweather_dict["weather"][0]["description"])
