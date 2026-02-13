from typing import TYPE_CHECKING
from os import system
from logging import getLogger

logger = getLogger(__file__)

if TYPE_CHECKING:
    from modules.search_cmd import Command


def execute_command(command: Command):
    logger.info("Running command: \nphrase: {phrase}\nbash: {bash}".format(**command))
    system(command["bash"])


__all__ = ("execute_command",)
