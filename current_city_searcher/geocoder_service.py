"""Класс для поучения название города, в котором сейчас находится пользователь с помощью сервера geocoder"""

import geocoder

from .contracts import CurrentCitySearcherService
from errors.errors import CantGetUserCityError


class GeocoderService(CurrentCitySearcherService):
    """Получает название города, в котором сейчас находится пользователь с помощью сервера geocoder"""
    def get_current_city(self) -> str:
        """
        Получает название города, в котором сейчас находится пользователь
        Params: -
        Returns: название города
        """
        try:
            geodata = geocoder.ip("me")
            return geodata.city
        except Exception:
            raise CantGetUserCityError()
