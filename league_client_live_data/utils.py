"""
provides utility functions
"""
import logging
from pathlib import Path

import yaml

from .config import Config

logger = logging.getLogger(__name__)


def load_config(path: Path) -> Config:
    """
    Load the config file
    :param path: path to config file
    :return: Config object
    """
    with open(path, "r", encoding="utf-8") as file:
        config = Config(**yaml.load(file, Loader=yaml.Loader))
        logger.debug("loaded config: %s", config)
        return config
