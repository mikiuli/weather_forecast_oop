from enum import StrEnum

from .actions import GetLocalWeather, GetWeatherbyCityName, GetWeatherHistory, DeleteWeatherHistory, ExitApp
from weather_storage import StorageCreator
from lexicon.lexicon_ru import Text
from weather_storage.storages.contracts import Storage


class Action(StrEnum):
    WEATHER_IN_USER_LOCATION = "1"
    WEATHER_IN_CITY = "2"
    WEATHER_REQUESTS_HISTORY = "3"
    DELETE_HISTORY = "4"
    APP_EXIT = "5"


class App:
    def __init__(self):
        with StorageCreator().create_weather_storage() as storage:
            while True:
                self.execute_action(storage)

    def get_action_by_number(self, number: str) -> str:
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

    def execute_action(self, storage: Storage) -> None:
        """
        Выполняет действие пользователя по номеру из списка
        Params: storage - хранилище данных о погоде
        Returns: -
        """
        print(Text.start_text)
        user_input = input().strip().lower()
        try:
            action = self.get_action_by_number(user_input)
            try:
                action_execution = action()
                action_execution.execute_action(storage)
            except TypeError:
                action.execute_action()
        except KeyError:
            print(Text.wrong_text)
