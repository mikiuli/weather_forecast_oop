"""Хранение погоды в виде текстового файла"""

from enum import StrEnum

from weather_getter.weather_api_services import Weather


class TextFileStorageInfo(StrEnum):
    """Параметры для создания текстового файла"""
    file_name = "weather_storage.txt"
    encoding = "utf-8"


class TextFileStorage:
    """
    Хранение погоды в виде текстового файла
    """
    def __enter__(self):
        self.file = open(TextFileStorageInfo.file_name, "a+", encoding=TextFileStorageInfo.encoding)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.file.close()

    def save_weather_data(self, data: Weather) -> None:
        """
        Сохраняет запрос прогноза погоды
        Params: data - прогноз погоды в виде класса Weather
        Returns: -
        """
        city_weather_info = (f"{data.current_time}&{data.city}&{data.weather_type}&{data.temperature}"
                             f"&{data.temperature_feels_like}&{data.wind_speed}\n")
        self.file = open(TextFileStorageInfo.file_name, "a", encoding=TextFileStorageInfo.encoding)
        self.file.write(city_weather_info)
        self.file.close()

    def get_weather_data(self, number: int) -> list[Weather]:
        """
        Получает историю последних запросов пользователя
        Params: number - количество запросов в виде целого числа
        Returns: список запросов в виде класса Weather
        """
        self.file = open(TextFileStorageInfo.file_name, "r", encoding=TextFileStorageInfo.encoding)
        city_weather_infos_list = self.file.readlines()
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
        return weather_datas_list

    def delete_weather_data(self):
        """
        Удаляет историю запросов погоды
        Params: -
        Returns: -
        """
        self.file = open(TextFileStorageInfo.file_name, "w", encoding=TextFileStorageInfo.encoding)
        self.file.close()