"""Декораторы для функций из weather_forecast для отлова предполагаемых ошибок"""

import sys
from typing import Callable
from functools import wraps

from errors.errors import MyBaseError


def errors_manager(func) -> Callable:
    """
    Декоратор
    Отлавливает пользовательские ошибки и завершает работу программы
    при наличии ошибок
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except MyBaseError as e:
            print(e)
            sys.exit()
    return wrapper
