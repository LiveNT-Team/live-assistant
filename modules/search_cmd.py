import os
import json
from pathlib import Path
from typing import TypedDict
from config import config

DEFAULT_APPDATA: Appdata = {"cmd_list": []}


class Appdata(TypedDict):
    cmd_list: list[Command]


class Command(TypedDict):
    phrase: str
    bash: str


def get_appdata() -> Appdata:
    path = Path(config["appdata"].format(USER=os.getenv("USER")))
    if not os.path.exists(path.parent):
        os.mkdir(path.parent)
        with open(path, "w") as file:
            json.dump(DEFAULT_APPDATA, file)
            data = DEFAULT_APPDATA
    else:
        if not os.path.exists(path):
            with open(path, "w") as file:
                json.dump(DEFAULT_APPDATA, file)
                data = DEFAULT_APPDATA
        else:
            with open(path, "r") as file:
                data = json.load(file)

    return data


def get_bash_by_phrase(
    phrase: str,
    appdata: Appdata = get_appdata(),
) -> Command | None:
    for command in appdata["cmd_list"]:
        if command["phrase"] == phrase:
            return command

    return None


__all__ = (
    "get_bash_by_phrase",
    "get_appdata",
)
