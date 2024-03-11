"""Интерфейс класса для получения названия города, в котором сейчас находится пользователь"""

from typing import Protocol


class CurrentCitySearcher(Protocol):
    """Интерфейс класса для получения названия города, в котором сейчас находится пользователь"""
    def get_current_city(self) -> str:
        """
        Получает название города, в котором сейчас находится пользователь
        Params: -
        Returns: название города
        """
        raise NotImplementedError
