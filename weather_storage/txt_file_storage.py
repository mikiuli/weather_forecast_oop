"""Хранение погоды в виде текстового файла"""

from enum import StrEnum

from .contracts import Storage
from models.weather import Weather
from configs.configs import get_production_storage_name
from logs.logers.logers import Loger


class TextFileStorageInfo(StrEnum):
    """Параметры для создания текстового файла"""
    encoding = "utf-8"


class TextFileStorage(Storage):
    """
    Хранение погоды в виде текстового файла
    """
    def __init__(self, file_name: str = get_production_storage_name()):
        self._file_name = f"{file_name}.txt"

    def __enter__(self):
        Loger().info(module=__name__,
                     msg=f"Создаю текстовый файл {self._file_name}, если его не существует, закрываю его")
        self.file = open(self._file_name, "a+", encoding=TextFileStorageInfo.encoding)
        self.file.close()
        Loger().info(module=__name__,
                     msg=f"Отправляю экземпляр класса {__class__.__name__}")
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        Loger().info(module=__name__,
                     msg="Закрываю соединение с текстовым файлом")
        self.file.close()

    def save_weather_data(self, data: Weather) -> None:
        """
        Сохраняет запрос прогноза погоды
        Params: data - прогноз погоды в виде класса Weather
        Returns: -
        """
        city_weather_info = (f"{data.current_time}&{data.city}&{data.weather_type}&{data.temperature}"
                             f"&{data.temperature_feels_like}&{data.wind_speed}\n")
        Loger().info(module=__name__,
                     msg="Открываю текстовый файл для записи")
        self.file = open(self._file_name, "a", encoding=TextFileStorageInfo.encoding)
        self.file.write(city_weather_info)
        Loger().info(module=__name__,
                     msg="Сохраняю данные, закрывая файл")
        self.file.close()

    def get_weather_data(self, number: int) -> list[Weather]:
        """
        Получает историю последних запросов пользователя
        Params: number - количество запросов в виде целого числа
        Returns: список запросов в виде класса Weather
        """
        Loger().info(module=__name__,
                     msg="Открываю текстовый файл для чтения")
        self.file = open(self._file_name, "r", encoding=TextFileStorageInfo.encoding)
        city_weather_infos_list = self.file.readlines()
        Loger().info(module=__name__, msg="Закрываю файл")
        self.file.close()

        city_weather_infos_list.reverse()
        weather_datas_list = []
        for weather_id in range(number if number < len(city_weather_infos_list) else len(city_weather_infos_list)):
            city_weather_info = city_weather_infos_list[weather_id].strip().split("&")
            weather_datas_list.append(Weather(current_time=city_weather_info[0],
                                              city=city_weather_info[1],
                                              weather_type=city_weather_info[2],
                                              temperature=int(city_weather_info[3]),
                                              temperature_feels_like=int(city_weather_info[4]),
                                              wind_speed=int(city_weather_info[5])))
        Loger().info(module=__name__,
                     msg="Отправляю данные о предыдущих запросах прогноза погоды в виде списка")
        return weather_datas_list

    def delete_weather_data(self):
        """
        Удаляет историю запросов погоды
        Params: -
        Returns: -
        """
        Loger().info(module=__name__,
                     msg="Обновляю файл, стирая все предыдущие записи")
        self.file = open(self._file_name, "w", encoding=TextFileStorageInfo.encoding)
        self.file.close()
