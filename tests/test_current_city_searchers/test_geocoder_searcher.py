"""Тестирование модуля current_city_searcher.geocoder_service"""

from current_city_searcher.geocoder_searcher import GeocoderSearcher


# pytest ./tests/test_current_city_searchers/test_geocoder_searcher.py

class TestGeocoderSearcher:
    """Тесты для GeocoderSearcher"""
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.city_service = GeocoderSearcher()

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_current_city(self):
        assert self.city_service.get_current_city() == "Saint Petersburg"
