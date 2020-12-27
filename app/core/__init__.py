from os import getenv
from functools import lru_cache

from .config import DevelopmentConfig
from .config import ProductionConfig


@lru_cache()
def get_settings():
    env = getenv("ENV", None)
    if env:
        return ProductionConfig()
    return DevelopmentConfig()
