from fastapi import FastAPI
from typing import Union
from app.core import ProductionConfig
from app.core import DevelopmentConfig
from app.core import get_settings


settings: Union[ProductionConfig, DevelopmentConfig]  = get_settings()


def create_app():

    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.DESCRIPTION,
        docs_url=settings.OPEN_API_URL,
        openapi_url=settings.OPEN_JSON_URL
    )

    return app
