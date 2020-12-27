from os import getenv
from os.path import abspath
from os.path import dirname

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    APP_DIR = abspath(dirname(dirname(__file__)))
    BASE_DIR = abspath(dirname(APP_DIR))
    APP_NAME: str = "JCB_HOME"
    SERVER_NAME: str = "JCB_SERVICE"
    ADMIN_EMAIL: str = "fxtafreeman@163.com"
    OPEN_API_URL: str = "/api/docs"
    OPEN_JSON_URL: str = "/api/openapi.json"
    LOGS_DIR: str = BASE_DIR
    DESCRIPTION: str = "johnny love chloe"
    JWT_TOKEN_PREFIX: str = "token"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1

    class Config:
        case_sensitive = True


class ProductionConfig(Settings):
    DEBUG: bool = False
    LOG_LEVEL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        case_sensitive = True


class DevelopmentConfig(Settings):
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    SECRET_KEY: str = getenv("SECRET_KEY", "(-ASp+_)-hw0848hnvVG-iqKyJSD&*&^-H3C9mqEqSl8KN-YRzRE")

    class Config:
        case_sensitive = True
