

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
