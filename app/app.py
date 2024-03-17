"""Запуск приложения"""

from enum import StrEnum

from .action_executors import GetLocalWeather, GetWeatherbyCityName, GetWeatherHistory, DeleteWeatherHistory, ExitApp

from .services_settings import get_storage

from lexicon.lexicon_ru import Text
from weather_storage.contracts import Storage


class Action(StrEnum):
    WEATHER_IN_USER_LOCATION = "1"
    WEATHER_IN_CITY = "2"
    WEATHER_REQUESTS_HISTORY = "3"
    DELETE_HISTORY = "4"
    APP_EXIT = "5"


class App:
    def __init__(self):
        self.start_app()

    def start_app(self):
        with get_storage() as storage:
            while True:
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
        Выполняет действие пользователя по номеру из списка
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        print(Text.start_text)
        user_input = input().strip().lower()
        try:
            action = self._get_action_by_number(user_input)
            try:
                action_execution = action()
                action_execution.execute_action(storage)
            except TypeError:
                action.execute_action()
        except KeyError:
            print(Text.wrong_text)
