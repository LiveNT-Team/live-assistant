import os
import json
from pathlib import Path
from typing import TypedDict

DEFAULT_CONFIG: Config = {
    "ai_api_key": None,
    "ai_api_url": None,
    "appdata": "/home/{USER}/.local/share/live-assistant/appdata.json",
}


class Config(TypedDict):
    ai_api_key: str
    ai_api_url: str
    appdata_filename: str


def load_config(
    path: Path | str = Path(
        f"/home/{os.getenv("USER")}/.config/live-assistant/config.json"
    ),
) -> Config:
    if not isinstance(path, Path):
        path = Path(path)

    if path.is_dir():
        raise ValueError("path не может быть директорией")

    if not os.path.exists(path.parent):
        os.makedirs(path.parent)
        with open(path, "w") as file:
            json.dump(DEFAULT_CONFIG, file)
            data: Config = DEFAULT_CONFIG
    else:
        with open(path, "r") as file:
            data: Config = json.load(file)

    return data


config = load_config()

__all__ = (
    "config",
    "load_config",
    "Config",
)
