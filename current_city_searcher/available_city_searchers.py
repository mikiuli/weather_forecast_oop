"""Доступные сервисы для получения города пользователя"""

from enum import Enum

from .geocoder_service import GeocoderService
from .ipinfo_service import IpinfoService


class AvailableCitySearcher(Enum):
    """Доступные сервисы для получения города пользователя"""
    geocoder = GeocoderService
    ipinfo = IpinfoService
