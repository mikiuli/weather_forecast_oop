"""Выполнение действий пользователя по введенному номеру"""

from typing import Protocol

import sys

from lexicon import Text
from errors import WrongCityName
from decorators import errors_manager

from weather_storage.storages.contracts import Storage
from current_city_searcher.current_city_searcher import CurrentCitySearcher
from weather_getter import WeatherGetter


class ActionExecutor(Protocol):
    def execute_action(self, storage: Storage) -> None:
        raise NotImplementedError


class GetLocalWeather(ActionExecutor):
    @errors_manager
    def execute_action(self, storage: Storage) -> None:
        """
        Получает погоду по местоположению пользователя
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        city_name = CurrentCitySearcher().get_city()
        weather = WeatherGetter().get_weather(city_name)
        storage.save_weather_data(weather)
        print(weather)


class GetWeatherbyCityName(ActionExecutor):
    @errors_manager
    def execute_action(self, storage: Storage) -> None:
        """
        Получает погоду по названию города
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        print(Text.print_city_name_text)
        city_name = input().strip().lower()
        while True:
            try:
                weather = WeatherGetter().get_weather(city_name)
                break
            except WrongCityName:
                print(Text.wrong_city_name_text)
                city_name = input().strip().lower()
                weather = WeatherGetter().get_weather(city_name)
        storage.save_weather_data(weather)
        print(weather)


class GetWeatherHistory(ActionExecutor):
    @errors_manager
    def execute_action(self, storage: Storage) -> None:
        """
        Получает историю запросов погоды
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        print(Text.requests_number_text)
        weather_data_number = input().strip().lower()
        while True:
            try:
                if "." in weather_data_number:
                    raise ValueError
                weather_data_number = int(weather_data_number)
                if weather_data_number < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print(Text.wrong_text)
                weather_data_number = input().strip().lower()
        weather_datas_list = storage.get_weather_data(int(weather_data_number))
        for number, weather_data in enumerate(weather_datas_list, 1):
            print("--------------"+str(number)+"--------------")
            print(weather_data)


class DeleteWeatherHistory(ActionExecutor):
    @errors_manager
    def execute_action(self, storage: Storage) -> None:
        """
        Удаляет историю запросов погоды
        Params: storage - хранилище данных о погоде
        Returns: -
            """
        storage.delete_weather_data()
        print(Text.delete_history_text)


class ExitApp(ActionExecutor):
    @staticmethod
    def execute_action() -> None:
        """
        Выход из приложения
        Params: -
        Returns: -
        """
        sys.exit(0)
