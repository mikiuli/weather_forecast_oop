"""Декораторы для отлова кастомных исключений"""

import sys
from typing import Callable
from functools import wraps

from errors.errors import MyBaseError
from logs.logers.logers import Loger


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
            Loger().critical(module=__name__, msg=f"Ошибка {e} была отловлена, завершаю работу приложения")
            print(e)
            sys.exit()
    return wrapper
