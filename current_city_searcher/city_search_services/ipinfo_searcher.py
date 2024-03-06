"""Класс для поучения название города, в котором сейчас находится пользователь, используя библиотеку ipinfo"""

import ipinfo
from environs import Env


class IpinfoSearcher:
    """Возвращает текущие координаты пользователя, используя библиотеку ipinfo"""
    def get_current_city(self) -> str:
        """
        Получает название города пользователя с помощью ipinfo
        params: -
        returns: Название города в виде строки
        """
        ipinfo_access_token = IpinfoSearcher.get_ipinfo_access_token()
        handler = ipinfo.getHandler(access_token=ipinfo_access_token)
        details = handler.getDetails()
        return details.city

    @staticmethod
    def get_ipinfo_access_token() -> str:
        """
        Получает токен доступа от ipinfo из переменных окружения
        Params: -
        Returns: токен доступа от ipinfo
        """
        env = Env()
        env.read_env()
        ipinfo_access_token = env("IPINFO_ACCESS_TOKEN")
        return ipinfo_access_token
