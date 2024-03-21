"""Содержит датакласс Weather"""

from typing import TypeAlias
from dataclasses import dataclass
from datetime import datetime

Celsius: TypeAlias = int
MetresPerSec: TypeAlias = int


@dataclass(slots=True, frozen=True)
class Weather:
    """Датакласс для стандартизации вида прогноза погоды"""
    current_time: datetime
    city: str
    weather_type: str
    temperature: Celsius
    temperature_feels_like: Celsius
    wind_speed: MetresPerSec

    def __repr__(self) -> str:
        """
        Форматирует экземпляр класса для вывода в консоль
        Params: -
        Returns: строка с информацией о погоде
        """
        return (f"Текущее время: {self.current_time}\n"
                f"Название города: {self.city}\n"
                f"Погодные условия: {self.weather_type}\n"
                f"Текущая температура: {self.temperature} "
                f"градус{Weather._format_gradus_ending(self.temperature)} по цельсию\n"
                f"Ощущается как: {self.temperature_feels_like} "
                f"градус{Weather._format_gradus_ending(self.temperature_feels_like)}"
                " по цельсию\n"
                f"Скорость ветра: {self.wind_speed} м/с\n")

    @staticmethod
    def _format_gradus_ending(temp: Celsius) -> str:
        """
        Изменяет окончание слова "градус" в зависимости от числительного
        перед ним
        Params: temp: температура в цельсиях
        Returns: окончание для слова "градус"
        """
        if str(temp)[-1] == "1" and abs(temp) != 11:
            return ""
        elif (str(temp)[-1] in
              ["2", "3", "4"]) and (abs(temp) not in
                                    [12, 13, 14]):
            return "a"
        else:
            return "ов"
