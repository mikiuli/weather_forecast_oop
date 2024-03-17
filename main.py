from app.app import App
from errors.errors import MyBaseError
from lexicon import Text


def main() -> None:
    """
    Запускает приложение
    Params: -
    Returns: -
    """
    App()


if __name__ == "__main__":
    try:
        main()
    except MyBaseError as e:
        print(e)
    except Exception:
        print(Text.app_cant_work_text)
