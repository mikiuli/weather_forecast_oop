from app.app import App
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
    except Exception:
        print(Text.app_cant_work_text)
