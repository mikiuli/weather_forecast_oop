"""Класс для поучения название города, в котором сейчас находится пользователь, используя библиотеку ipinfo"""

import ipinfo
import requests

from .contracts import CurrentCitySearcherService
from configs.configs import get_ipinfo_access_token
from errors.errors import CantGetUserCityError
from logs.logers.logers import Loger


class IpinfoService(CurrentCitySearcherService):
    """Возвращает город пользователя, используя библиотеку ipinfo"""
    def get_current_city(self) -> str:
        """
        Получает название города пользователя с помощью ipinfo
        params: -
        returns: Название города в виде строки
        """
        ipinfo_access_token = get_ipinfo_access_token()
        try:
            handler = ipinfo.getHandler(access_token=ipinfo_access_token)
            details = handler.getDetails()
            city = details.city
            Loger().info(module=__name__, msg="Получаю название города")
            return city
        except requests.exceptions.ConnectionError:
            raise CantGetUserCityError()
