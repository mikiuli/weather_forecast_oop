"""Хранение погоды в базе данных sqlite3"""

from enum import Enum

import sqlite3

from .contracts import Storage
from errors.errors import NoConnectionWithDBError
from models.weather import Weather
from configs.configs import get_production_storage_name
from logs.logers.logers import Loger


class Query(Enum):
    CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY,
        time TEXT NOT NULL,
        city_name TEXT NOT NULL,
        weather_type TEXT NOT NULL,
        temperature INTEGER NOT NULL,
        temp_feels_like INTEGER NOT NULL,
        wind_speed INTEGER NOT NULL
    )"""
    CREATE_INDEX_QUERY = """CREATE INDEX idx_id ON weather_data (id)"""
    COUNT_REQUESTS_QUERY = """SELECT COUNT(*) FROM weather_data"""
    INSERT_QUERY = """INSERT INTO weather_data (time, city_name, weather_type,
    temperature, temp_feels_like, wind_speed) VALUES (?, ?, ?, ?, ?, ?)"""
    DELETE_ALL_REQUESTS_QUERY = """DELETE FROM weather_data"""
    SELECT_LAST_N_REQUESTS_QUERY = """SELECT time, city_name, weather_type,
    temperature, temp_feels_like, wind_speed FROM weather_data
    ORDER BY id DESC
    LIMIT {number}"""


class SQLiteStorage(Storage):
    """Хранение погоды в базе данных sqlite3"""

    def __init__(self, db_name: str = get_production_storage_name()) -> None:
        self._db_name = f"{db_name}.db"

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self._db_name)
            self._init_table()
            Loger().info(module=__name__,
                         msg=f"Отправляю экземпляр класса {__class__.__name__} с открытым соединением с базой данных")
            return self
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        Loger().info(module=__name__,
                     msg="Закрываю соединение с базой данных")
        self.connection.close()

    def _init_table(self) -> None:
        """
        Создает таблицу в базе данных
        params: -
        returns: -
        """
        try:
            cursor = self.connection.cursor()

            Loger().info(module=__name__,
                         msg="Создаю таблицу для хранения погоды, если её нет в базе данных")
            cursor.execute(Query.CREATE_TABLE_QUERY.value)
            try:
                Loger().info(module=__name__,
                             msg="Создаю индексы для таблицы")
                cursor.execute(Query.CREATE_INDEX_QUERY.value)
            except sqlite3.OperationalError:
                Loger().info(module=__name__,
                             msg="Индексы уже есть")
                pass

            Loger().info(module=__name__,
                         msg="Сохраняю изменения")
            self.connection.commit()
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def save_weather_data(self, data) -> None:
        """
        Сохраняет запрос прогноза погоды
        Params: data - прогноз погоды в виде класса Weather
        Returns: -
        """
        try:
            cursor = self.connection.cursor()

            Loger().info(module=__name__,
                         msg="Сохраняю данные в таблицу")
            cursor.execute(Query.INSERT_QUERY.value, (data.current_time, data.city, data.weather_type,
                                                      data.temperature, data.temperature_feels_like,
                                                      data.wind_speed))

            Loger().info(module=__name__,
                         msg="Сохраняю изменения")
            self.connection.commit()
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def get_weather_data(self, number) -> list[Weather]:
        """
        Получает историю последних запросов пользователя
        Params: number - количество запросов в виде целого числа
        Returns: список запросов в виде класса Weather
        """
        try:
            cursor = self.connection.cursor()

            Loger().info(module=__name__,
                         msg=f"Получаю данные о запросах прогноза погоды из базы данных в количестве {number}")
            cursor.execute(Query.SELECT_LAST_N_REQUESTS_QUERY.value.format(number=number))
            weather_datas = cursor.fetchall()

            weather_datas_list = []
            for data in weather_datas:
                weather = Weather(current_time=data[0], city=data[1], weather_type=data[2],
                                  temperature=data[3], temperature_feels_like=data[4], wind_speed=data[5])
                weather_datas_list.append(weather)

            Loger().info(module=__name__,
                         msg="Отправляю данные о предыдущих запросах прогноза погоды в виде списка")
            return weather_datas_list
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def delete_weather_data(self) -> None:
        """
        Удаляет историю запросов погоды
        Params: -
        Returns: -
        """
        try:
            cursor = self.connection.cursor()

            Loger().info(module=__name__,
                         msg="Удаляю все запросы прогноза погоды из базы данных")
            cursor.execute(Query.DELETE_ALL_REQUESTS_QUERY.value)

            Loger().info(module=__name__,
                         msg="Сохраняю изменения")
            self.connection.commit()
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()
