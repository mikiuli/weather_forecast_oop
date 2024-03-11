"""Получение названия города пользователя"""

from .current_city_searchers import CurrentCitySearcher, GeocoderSearcher, IpinfoSearcher
from errors import errors


def get_city() -> str:
    """
    Получает город, где находится пользователь
    Params: -
    Returns: название города
    """
    city_searcher = _get_city_searcher("ipinfo")
    try:
        city_name = city_searcher.get_current_city()
    except Exception:
        raise errors.CantGetUserCityError()
    return city_name


def _get_city_searcher(name: str) -> CurrentCitySearcher:
    """
    Выбирает сервис для определения города пользователя
    Params: name - название сервиса
    Returns: экземпляр класса сервиса
    """
    searchers_by_name = {
        "geocoder": GeocoderSearcher,
        "ipinfo": IpinfoSearcher,
    }
    return searchers_by_name.get(name)()
