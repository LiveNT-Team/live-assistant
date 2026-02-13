import json
from os.path import exists
from os import makedirs, getenv
from pathlib import Path

DEFAULT_SETTINGS = {"ai_api_key": None, "ai_api_url": None}


class Config:
    """
    Класс `Config` представляет собой класс, при создании экземпляра которого импортирует настройки из файла конфигурации в виде свойств экземпляра

    Пример получение значения:

    > config = Config()
    > config.variable
    'foo'
    """

    ai_api_key: str
    ai_api_url: str

    def __init__(
        self,
        path: str | Path = Path(
            f"/home/{getenv("USER")}/.config/live-assistant/config.json"
        ),
    ):
        """
        Импортирует данные из файла, если файл не найден он будет создан

        :param path: Путь к файлу конфигурации
        :type path: str | Path
        """
        # Преобразуем путь в экземпляр Path если надо
        self.path = path
        if not isinstance(self.path, Path):
            self.path = Path(self.path)

        # Если это каталог, вызвать ошибку
        if self.path.is_dir():
            raise ValueError("Неверный путь к файлу конфигурации")

        # Если такого каталога не существует - создать
        if not exists(self.path.parent):
            makedirs(self.path.parent)

        # Если файл не существует - создать
        if not exists(self.path):
            with open(self.path, "w") as file:
                json.dump(DEFAULT_SETTINGS, file)

            self._data = DEFAULT_SETTINGS
        else:
            with open(self.path, "r") as file:
                self._data = json.load(file)

        self.__dict__.update(self._data)


config = Config()

__all__ = ("config",)
