"""Получение названия города пользователя"""

from .current_city_searchers import CurrentCitySearcher, GeocoderSearcher, IpinfoSearcher
from errors import errors


class CitySearcherService:
    """Сервис для получения названия текущего города пользователя
    с использованием выбранной библиотеки"""
    def __init__(self):
        self.selected_searcher = "ipinfo"
        self.searchers_by_name = {
            "geocoder": GeocoderSearcher,
            "ipinfo": IpinfoSearcher,
        }

    def get_city(self) -> str:
        """
        Получает город, где находится пользователь
        Params: -
        Returns: название города
        """
        city_searcher = self._get_city_searcher()
        try:
            city_name = city_searcher.get_current_city()
        except Exception:
            raise errors.CantGetUserCityError()
        return city_name

    def _get_city_searcher(self) -> CurrentCitySearcher:
        """
        Выбирает сервис для определения города пользователя
        Params: name - название сервиса
        Returns: экземпляр класса сервиса
        """
        return self.searchers_by_name.get(self.selected_searcher)()
