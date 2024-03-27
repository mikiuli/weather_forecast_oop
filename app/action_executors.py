"""Выполнение действий пользователя по введенному номеру"""

from typing import Protocol

import sys

from lexicon import Text
from errors import WrongCityName
from decorators import errors_manager

from weather_storage.contracts import Storage
from weather_getter import OpenWeatherapiService
from current_city_searcher import IpinfoSearcher
from logs.logers.logers import Loger


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
        city_name = IpinfoSearcher().get_current_city()
        Loger().info(module=__name__, msg=f"Получила город {city_name}")

        weather = OpenWeatherapiService().get_weather_by_city(city_name)
        Loger().info(module=__name__, msg=f"Получаю погоду \n{str(weather)}перехожу к сохранению в хранилище")

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
        Loger().info(module=__name__, msg=f"Получаю от пользователя потенциальное название города города {city_name}")

        while True:
            try:
                weather = OpenWeatherapiService().get_weather_by_city(city_name)
                Loger().info(module=__name__, msg=f"Получаю погоду \n{str(weather)}перехожу к сохранению в хранилище")
                break

            except WrongCityName as e:
                Loger().info(module=__name__, msg=f"Введено некоректное название города, вернулась ошибка {e}")
                print(Text.wrong_city_name_text)

                Loger().info(module=__name__, msg="Запрашиваю название города снова")
                city_name = input().strip().lower()

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
        Loger().info(module=__name__,
                     msg="Получаю количество запросов, которые хочет получить пользователь из хранилища")
        weather_data_number = input().strip().lower()

        Loger().info(module=__name__, msg="Проверяю, ввёл ли пользователь целое число")
        while True:
            try:
                if "." in weather_data_number:
                    raise ValueError
                Loger().info(module=__name__, msg="Пытаюсь преобразовать к целому числу")
                weather_data_number = int(weather_data_number)
                if weather_data_number < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                Loger().info(module=__name__, msg=f"Невалидный ввод {weather_data_number}")
                print(Text.wrong_text)
                weather_data_number = input().strip().lower()

        Loger().info(module=__name__,
                     msg="Получаю данные о предыдущих запросах прогноза погоды в виде списка из хранилища")
        weather_datas_list = storage.get_weather_data(weather_data_number)
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
        Loger().info(module=__name__, msg="Удаляю всю информацию о запросах погоды из хранилища")
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
        Loger().info(module=__name__, msg="Выхожу из приложения")
        sys.exit(0)
