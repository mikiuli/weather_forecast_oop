from api_services.weather import Weather
from api_services.contracts import WeatherGetter
from api_services.openweathermap_service import OpenWeatherapiGetter

from current_city_searchers.contracts import CurrentCitySearcher
from current_city_searchers.ipinfo_searcher import IpinfoSearcher
from current_city_searchers.geocoder_searcher import GeocoderSearcher

from storages.contracts import Storage
from storages.sqlite_storage import SQLiteStorage
from storages.txt_file_storage import TextFileStorage
from storages.list_storage import ListStorage


class Service:
    """
    Промежуточный слой между бизнес-логикой и сервисами, необходимыми для работы приложения
    Выбор API-сервера, хранилища, способа получения текущего местоположения пользователя
    """
    def __init__(self):
        self._create_weather_storage()

    def _create_weather_storage(self) -> None:
        self.weather_storage = self._get_weather_storage("sqlite3")

    def _get_weather_storage(self, name: str) -> Storage:
        storages = {
            "sqlite3": SQLiteStorage,
            "weather_storage.txt": TextFileStorage,
            "list": ListStorage,
        }
        return storages.get(name)()

    def get_city(self):
        city_searcher = self._get_city_searcher("geocoder")
        city_name = city_searcher.get_current_city()
        return city_name

    def _get_city_searcher(self, name: str) -> CurrentCitySearcher:
        searchers_by_name = {
            "geocoder": GeocoderSearcher,
            "ipinfo": IpinfoSearcher,
        }
        return searchers_by_name.get(name)()

    def get_weather(self, city_name: str) -> Weather:
        weather_getter = self._get_weather_getter("openweathermap.org")
        weather = weather_getter.get_weather_by_city(city_name)
        return weather

    def _get_weather_getter(self, name: str) -> WeatherGetter:
        weather_getters_by_name = {
            "openweathermap.org": OpenWeatherapiGetter,
        }
        return weather_getters_by_name.get(name)()

    def save_weather_data(self, data: Weather) -> None:
        self.weather_storage.save_weather_data(data)

    def get_weather_data(self, number: int) -> list[Weather]:
        weather_datas_list = self.weather_storage.get_weather_data(number)
        return weather_datas_list

    def delete_weather_data(self) -> None:
        self.weather_storage.delete_weather_data()

    def to_close_app(self) -> None:
        self.weather_storage.to_close()
