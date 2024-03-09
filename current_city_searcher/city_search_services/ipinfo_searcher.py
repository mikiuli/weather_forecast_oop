"""Класс для поучения название города, в котором сейчас находится пользователь, используя библиотеку ipinfo"""

import ipinfo

from configs.configs import get_ipinfo_access_token


class IpinfoSearcher:
    """Возвращает текущие координаты пользователя, используя библиотеку ipinfo"""
    def get_current_city(self) -> str:
        """
        Получает название города пользователя с помощью ipinfo
        params: -
        returns: Название города в виде строки
        """
        ipinfo_access_token = get_ipinfo_access_token()
        handler = ipinfo.getHandler(access_token=ipinfo_access_token)
        details = handler.getDetails()
        return details.city
