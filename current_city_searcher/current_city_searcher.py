"""Получение названия города пользователя"""

from .city_searching_services import CurrentCitySearcherService, GeocoderService, IpinfoService
from errors import errors


class CurrentCitySearcher:
    """Сервис для получения названия текущего города пользователя
    с использованием выбранной библиотеки"""
    def __init__(self):
        self.selected_service = "ipinfo"
        self.services_by_name = {
            "geocoder": GeocoderService,
            "ipinfo": IpinfoService,
        }

    def get_city(self) -> str:
        """
        Получает город, где находится пользователь
        Params: -
        Returns: название города
        """
        city_searching_service = self._get_city_searching_service()
        try:
            city_name = city_searching_service.get_current_city()
        except Exception:
            raise errors.CantGetUserCityError()
        return city_name

    def _get_city_searching_service(self) -> CurrentCitySearcherService:
        """
        Выбирает сервис для определения города пользователя
        Params: -
        Returns: экземпляр класса сервиса
        """
        return self.services_by_name.get(self.selected_service)()
