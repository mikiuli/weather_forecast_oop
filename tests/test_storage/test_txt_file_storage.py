from tests.fixtures.storage_sample_creator import text_storage
from tests.fixtures.weather_samples import weather_data_samples

__all__ = [text_storage, weather_data_samples, ]

# pytest ./tests/test_storage/test_txt_file_storage.py


class TestTxtFileStorage:
    def setup_method(self):
        self.data_length = 3
        self.less_lenght_data = 2

    def test_add_and_get_data(self, text_storage, weather_data_samples):
        for data in weather_data_samples:
            text_storage.save_weather_data(data=data)
        assert text_storage.get_weather_data(number=self.data_length) == list(reversed(weather_data_samples))

    def test_add_and_delete_data(self, text_storage, weather_data_samples):
        for data in weather_data_samples:
            text_storage.save_weather_data(data=data)
        text_storage.delete_weather_data()
        assert text_storage.get_weather_data(number=self.data_length) == []

    def test_get_less_data(self, text_storage, weather_data_samples):
        for data in weather_data_samples:
            text_storage.save_weather_data(data=data)
        assert text_storage.get_weather_data(number=self.less_lenght_data
                                             ) == list(reversed(weather_data_samples))[:self.less_lenght_data]

    def test_get_zero_data(self, text_storage, weather_data_samples):
        for data in weather_data_samples:
            text_storage.save_weather_data(data=data)
        assert text_storage.get_weather_data(number=0) == []
