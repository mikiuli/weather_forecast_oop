from actions import execute_action
from lexicon import Text
from weather_storage import StorageCreator


def main() -> None:
    """
    Запускает приложение
    Params: -
    Returns: -
    """
    with StorageCreator().create_weather_storage() as storage:
        while True:
            execute_action(storage)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(Text.app_cant_work_text)
