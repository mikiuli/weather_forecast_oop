"""Запуск приложения"""

from enum import StrEnum

from .action_executors import GetLocalWeather, GetWeatherbyCityName, GetWeatherHistory, DeleteWeatherHistory, ExitApp

from weather_storage import SQLiteStorage

from lexicon.lexicon_ru import Text
from weather_storage.contracts import Storage
from logs.logers.logers import Loger


class Action(StrEnum):
    WEATHER_IN_USER_LOCATION = "1"
    WEATHER_IN_CITY = "2"
    WEATHER_REQUESTS_HISTORY = "3"
    DELETE_HISTORY = "4"
    APP_EXIT = "5"


class App:
    def __init__(self) -> None:
        Loger().info(module=__name__, msg="Создался экземпляр класса App")

    def start_app(self) -> None:
        """
        Запускает приложение, создаёт экземпляр хранилища
        Params: -
        Returns: -
        """
        with SQLiteStorage() as storage:
            Loger().info(module=__name__, msg="Получили экземпляр выбранного класса хранилища")
            self._create_loop(storage)

    def _get_action_by_number(self, number: str) -> str:
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

    def _create_loop(self, storage: Storage) -> None:
        """
        Создаёт бесконечный цикл, в котором выполняются действия пользователя
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        Loger().info(module=__name__, msg="Вошли в цикл")
        while True:
            print(Text.start_text)
            user_input = input().strip().lower()
            Loger().info(module=__name__, msg=f"Выполняю действие {user_input}")
            try:
                action = self._get_action_by_number(user_input)
                try:
                    action().execute_action(storage)
                except TypeError:
                    action().execute_action()
            except KeyError:
                Loger().info(module=__name__, msg="Такого действия нет")
                print(Text.wrong_text)
