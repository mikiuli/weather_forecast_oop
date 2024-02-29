from enum import StrEnum
import sys

from services import Service
from lexicon import Text
from errors import WrongCityName
from decorators import errors_manager


@errors_manager
def get_local_weather(service: Service) -> None:
    """
    Получает погоду по местоположению пользователя
    Params: service - экземпляр класса Service
    Returns: -
    """
    city_name = service.get_city()
    weather = service.get_weather(city_name)
    service.save_weather_data(weather)
    print(weather)


@errors_manager
def get_weather_by_city_name(service: Service) -> None:
    """
    Получает погоду по названию города
    Params: service - экземпляр класса Service
    Returns: -
    """
    print(Text.print_city_name_text)
    city_name = input().strip().lower()
    while True:
        try:
            weather = service.get_weather(city_name)
            break
        except WrongCityName:
            print(Text.wrong_city_name_text)
            city_name = input().strip().lower()
            weather = service.get_weather(city_name)
    service.save_weather_data(weather)
    print(weather)


@errors_manager
def get_weather_history(service: Service) -> None:
    """
    Получает историю запросов погоды
    Params: service - экземпляр класса Service
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
    weather_datas_list = service.get_weather_data(int(weather_data_number))
    for number, weather_data in enumerate(weather_datas_list, 1):
        print("--------------"+str(number)+"--------------")
        print(weather_data)


@errors_manager
def delete_weather_history(service: Service) -> None:
    """
    Удаляет историю запросов погоды
    Params: service - экземпляр класса Service
    Returns: -
    """
    service.delete_weather_data()
    print(Text.delete_history_text)


def exit_app() -> None:
    """
    Выход из приложения
    Params: -
    Returns: -
    """
    sys.exit()


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
        Action.WEATHER_IN_USER_LOCATION: get_local_weather,
        Action.WEATHER_IN_CITY: get_weather_by_city_name,
        Action.WEATHER_REQUESTS_HISTORY: get_weather_history,
        Action.DELETE_HISTORY: delete_weather_history,
        Action.APP_EXIT: exit_app,
    }
    return actions[number]


def execute_action(service: Service) -> None:
    """
    Выполняет действие пользователя по номеру из списка
    Params: service - экземпляр класса Service
    Returns: -
    """
    print(Text.start_text)
    user_input = input().strip().lower()
    try:
        action = get_action_by_number(user_input)
        try:
            action(service)
        except TypeError:
            action()
    except KeyError:
        print(Text.wrong_text)


def close_app(service: Service) -> None:
    """
    Выполняет необходимые для закрытия приложения действия
    Params: service - экземпляр класса Service
    Returns: -
    """
    service.to_close_app()


def main() -> None:
    """
    Запускает приложение
    Params: -
    Returns: -
    """
    servise = Service()
    try:
        while True:
            execute_action(servise)
    except Exception:
        print(Text.app_cant_work_text)
        raise Exception
    finally:
        close_app(servise)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(Text.app_cant_work_text)
