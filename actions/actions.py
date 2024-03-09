"""Выполнение действий пользователя по введенному номеру"""

from enum import StrEnum
from typing import Protocol

import sys

from lexicon import Text
from errors import WrongCityName
from decorators import errors_manager

from weather_storage.storages.contracts import Storage
from current_city_searcher import get_city
from weather_getter import get_weather


class Action(Protocol):
    def execute_action(self, storage: Storage) -> None:
        raise NotImplementedError


class GetLocalWeather(Action):
    @errors_manager
    def execute_action(self, storage: Storage) -> None:
        """
        Получает погоду по местоположению пользователя
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        city_name = get_city()
        weather = get_weather(city_name)
        storage.save_weather_data(weather)
        print(weather)


class GetWeatherbyCityName(Action):
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
                weather = get_weather(city_name)
                break
            except WrongCityName:
                print(Text.wrong_city_name_text)
                city_name = input().strip().lower()
                weather = get_weather(city_name)
        storage.save_weather_data(weather)
        print(weather)


class GetWeatherHistory(Action):
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


class DeleteWeatherHistory(Action):
    @errors_manager
    def execute_action(self, storage: Storage) -> None:
        """
        Удаляет историю запросов погоды
        Params: storage - хранилище данных о погоде
        Returns: -
            """
        storage.delete_weather_data()
        print(Text.delete_history_text)


class ExitApp(Action):
    @staticmethod
    def execute_action() -> None:
        """
        Выход из приложения
        Params: -
        Returns: -
        """
        sys.exit(0)


class Action(StrEnum):
    WEATHER_IN_USER_LOCATION = "1"
    WEATHER_IN_CITY = "2"
    WEATHER_REQUESTS_HISTORY = "3"
    DELETE_HISTORY = "4"
    APP_EXIT = "5"


def get_action_by_number(number: str) -> str:
    """
    Выбирает функцию по номеру из class Action
    Params: number - введённый пользователем номер
    Returns: название функции
    """
    actions = {
        Action.WEATHER_IN_USER_LOCATION: GetLocalWeather,
        Action.WEATHER_IN_CITY: GetWeatherbyCityName,
        Action.WEATHER_REQUESTS_HISTORY: GetWeatherHistory,
        Action.DELETE_HISTORY: DeleteWeatherHistory,
        Action.APP_EXIT: ExitApp,
    }
    return actions[number]


def execute_action(storage: Storage) -> None:
    """
    Выполняет действие пользователя по номеру из списка
    Params: storage - хранилище данных о погоде
    Returns: -
    """
    print(Text.start_text)
    user_input = input().strip().lower()
    try:
        action = get_action_by_number(user_input)
        try:
            action_execution = action()
            action_execution.execute_action(storage)
        except TypeError:
            action.execute_action()
    except KeyError:
        print(Text.wrong_text)
