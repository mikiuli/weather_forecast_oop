from app.app import App
from errors.errors import MyBaseError
from lexicon import Text
from logs.logers.logers import Loger


def main() -> None:
    """
    Запускает приложение
    Params: -
    Returns: -
    """
    Loger().info(module=__name__, msg="\n\n\n Запускаю приложение\n")
    App().start_app()


if __name__ == "__main__":
    try:
        main()
    except MyBaseError as e:
        Loger().critical(module=__name__, msg=f"Ошибка {e} была отловлена в {__name__}")
        print(e)
    except Exception:
        Loger().critical(module=__name__, msg=f"Ошибка отловлена в {__name__}", with_tb=True)
        print(Text.app_cant_work_text)
