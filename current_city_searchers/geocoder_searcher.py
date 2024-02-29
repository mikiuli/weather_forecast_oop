"""Класс для поучения название города, в котором сейчас находится пользователь с помощью сервера geocoder"""

import geocoder


class GeocoderSearcher:
    """Получает название города, в котором сейчас находится пользователь с помощью сервера geocoder"""
    def get_current_city(self) -> str:
        """
        Получает название города, в котором сейчас находится пользователь
        Params: -
        Returns: название города
        """
        geodata = geocoder.ip("me")
        return geodata.city
