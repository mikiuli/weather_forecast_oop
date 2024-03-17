from current_city_searcher.ipinfo_service import IpinfoService


# pytest ./tests/test_current_city_searchers/test_ipinfo_searcher.py

class TestIpinfoService:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.city_service = IpinfoService()

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_current_city(self):
        assert self.city_service.get_current_city() == "Saint Petersburg"
