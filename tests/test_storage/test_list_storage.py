from tests.fixtures.storage_sample_creator import list_storage
from tests.fixtures.weather_samples import weather_data_samples

all = [list_storage, weather_data_samples, ]

# pytest ./tests/test_storage/test_list_storage.py


class TestSQLiteStorage:
    def setup_method(self):
        self.data_length = 3
        self.less_lenght_data = 2

    def test_add_and_get_data(self, list_storage, weather_data_samples):
        for data in weather_data_samples:
            list_storage.save_weather_data(data=data)
        assert list_storage.get_weather_data(number=3) == list(reversed(weather_data_samples))

    def test_add_and_delete_data(self, list_storage, weather_data_samples):
        for data in weather_data_samples:
            list_storage.save_weather_data(data=data)
        list_storage.delete_weather_data()
        assert list_storage.get_weather_data(number=2) == []

    def test_get_less_data(self, list_storage, weather_data_samples):
        for data in weather_data_samples:
            list_storage.save_weather_data(data=data)
        assert list_storage.get_weather_data(number=self.less_lenght_data
                                             ) == list(reversed(weather_data_samples))[:self.less_lenght_data]

    def test_get_zero_data(self, list_storage, weather_data_samples):
        for data in weather_data_samples:
            list_storage.save_weather_data(data=data)
        assert list_storage.get_weather_data(number=0) == []
