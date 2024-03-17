from current_city_searcher.geocoder_service import GeocoderService


# pytest ./tests/test_current_city_searchers/test_geocoder_searcher.py

class TestGeocoderService:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.city_service = GeocoderService()

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_current_city(self):
        assert self.city_service.get_current_city() == "Saint Petersburg"
