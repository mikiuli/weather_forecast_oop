"""Хранение погоды в базе данных sqlite3"""

import sqlite3

from errors.errors import NoConnectionWithDBError
from api_services.weather import Weather

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


class SQLiteStorage:
    """
    Хранение погоды в базе данных sqlite3
    """
    def __init__(self):
        try:
            self.connection = sqlite3.connect("weather_forecast.db")
            self.cursor = self.connection.cursor()
            self._init_table(self.connection)
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def _init_table(self, connection: sqlite3.Connection) -> None:
        """
        Создает таблицу в базе данных
        params: connection: соединение с базой данных, открытое
        в функции connect_with_database
        returns: -
        """
        try:
            self.cursor.execute(CREATE_TABLE_QUERY)
            try:
                self.cursor.execute(CREATE_INDEX_QUERY)
            except sqlite3.OperationalError:
                pass
            connection.commit()
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def save_weather_data(self, data):
        """
        Сохраняет запрос прогноза погоды
        Params: data - прогноз погоды в виде класса Weather
        Returns: -
        """
        try:
            self.cursor.execute(INSERT_QUERY, (data.current_time, data.city, data.weather_type,
                                               data.temperature, data.temperature_feels_like, data.wind_speed))

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
            self.cursor.execute(SELECT_LAST_N_REQUESTS_QUERY.format(number=number))
            weather_datas = self.cursor.fetchall()

            weather_datas_list = []
            for data in weather_datas:
                weather = Weather(current_time=data[0], city=data[1], weather_type=data[2],
                                  temperature=data[3], temperature_feels_like=data[4], wind_speed=data[5])
                weather_datas_list.append(weather)
            return weather_datas_list
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def delete_weather_data(self):
        """
        Удаляет историю запросов погоды
        Params: -
        Returns: -
        """
        try:
            self.cursor.execute(DELETE_ALL_REQUESTS_QUERY)
            self.connection.commit()
        except sqlite3.OperationalError:
            raise NoConnectionWithDBError()

    def to_close(self) -> None:
        """
        Корректно закрывает соединение с хранилищем
        Params: -
        Returns: -
        """
        self.connection.close()
