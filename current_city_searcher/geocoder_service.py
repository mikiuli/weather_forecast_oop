"""Класс для поучения название города, в котором сейчас находится пользователь с помощью сервера geocoder"""

import geocoder

from .contracts import CurrentCitySearcherService
from errors.errors import CantGetUserCityError
from logs.logers.logers import Loger


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
            city = geodata.city
            Loger().info(module=__name__, msg="Получаю название города")
            if city is None:
                raise CantGetUserCityError()
            return city
        except Exception:
            raise CantGetUserCityError()
