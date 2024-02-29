"""Хранение погоды в виде списка"""

from copy import deepcopy

from api_services.weather import Weather


class ListStorage:
    """
    Хранение погоды в виде списка
    """
    def __init__(self) -> None:
        self.weather_storage_list = []

    def save_weather_data(self, data: Weather) -> None:
        """
        Сохраняет запрос прогноза погоды
        Params: data - прогноз погоды в виде класса Weather
        Returns: -
        """
        self.weather_storage_list.append(data)

    @staticmethod
    def _reverse_list(original_list: list) -> list:
        """
        Копирует и переворачивает список
        Params: original_list - список
        Returns: перевёрнутый список
        """
        list_copy = deepcopy(original_list)
        list_copy.reverse()
        return list_copy

    def get_weather_data(self, number: int) -> list[Weather]:
        """
        Получает историю последних запросов пользователя
        Params: number - количество запросов в виде целого числа
        Returns: список запросов в виде класса Weather
        """
        reversed_list = ListStorage._reverse_list(self.weather_storage_list)
        weather_datas_list = []
        for weather_id in range(number if number < len(self.weather_storage_list)
                                else len(self.weather_storage_list)):
            weather_datas_list.append(reversed_list[weather_id])
        return weather_datas_list

    def delete_weather_data(self) -> None:
        """
        Удаляет историю запросов погоды
        Params: -
        Returns: -
        """
        self.weather_storage_list = []

    def to_close(self) -> None:
        """
        Корректно закрывает соединение с хранилищем
        Params: -
        Returns: -
        """
        pass
