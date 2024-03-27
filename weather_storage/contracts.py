"""Интрфейс для класса, отвечающего за хренение истории запросов прогноза погоды"""

from typing import Protocol

from models.weather import Weather


class Storage(Protocol):
    """
    Интерфейс класса для хранилища информации о прогнозе погоды
    Должен поддерживать контекстный менеджер with
    """
    def save_weather_data(self, data: Weather) -> None:
        """
        Сохраняет запрос прогноза погоды
        Params: data - прогноз погоды в виде класса Weather
        Returns: -
        """
        raise NotImplementedError

    def get_weather_data(self, number: int) -> list[Weather]:
        """
        Получает историю последних запросов пользователя
        Params: number - количество запросов в виде целого числа
        Returns: список запросов в виде класса Weather
        """
        raise NotImplementedError

    def delete_weather_data(self) -> None:
        """
        Удаляет историю запросов погоды
        Params: -
        Returns: -
        """
        raise NotImplementedError
