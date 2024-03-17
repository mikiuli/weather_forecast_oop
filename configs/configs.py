"""Получение переменных среды"""

from environs import Env


def get_ipinfo_access_token() -> str:
    """
    Получает токен доступа от ipinfo из переменных окружения
    Params: -
    Returns: токен доступа от ipinfo
    """
    env = Env()
    env.read_env()
    ipinfo_access_token = env("IPINFO_ACCESS_TOKEN")
    return ipinfo_access_token


def get_openweather_key() -> str:
    """
    Получает ключ от openweathermap.org из переменных окружения
    Params: -
    Returns: ключ от openweathermap.org
    """
    env = Env()
    env.read_env()
    openweather_key = env("OPENWEATHER_API")
    return openweather_key


def get_production_storage_name() -> str:
    """
    Возвращает название хранилища
    Params: -
    Returns: название хранилища
    """
    env = Env()
    env.read_env()
    production_db_name = env("PRODUCTION_STORAGE_NAME")
    return production_db_name


def get_test_storage_name() -> str:
    """
    Возвращает название тестового хранилища
    Params: -
    Returns: название тестового хранилища
    """
    env = Env()
    env.read_env()
    test_db_name = env("TEST_STORAGE_NAME")
    return test_db_name
