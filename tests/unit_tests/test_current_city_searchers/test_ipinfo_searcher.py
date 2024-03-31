"""Тестирование модуля current_city_searcher.ipinfo_service"""

from current_city_searcher.ipinfo_searcher import IpinfoSearcher


# pytest ./tests/unit_tests/test_current_city_searchers/test_ipinfo_searcher.py

class TestIpinfoSearcher:
    """Тестирование IpinfoSearcher"""
    def setup_method(self):
        self.city_service = IpinfoSearcher()

    def test_current_city(self):
        assert self.city_service.get_current_city() == "Saint Petersburg"
