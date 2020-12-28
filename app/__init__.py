from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from typing import Union

from app.core import ProductionConfig
from app.core import DevelopmentConfig
from app.core import get_settings

from app.routers import router


settings: Union[ProductionConfig, DevelopmentConfig]  = get_settings()


def create_app():

    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.DESCRIPTION,
        docs_url=settings.OPEN_API_URL,
        openapi_url=settings.OPEN_JSON_URL,
    )

    app.mount("/static", StaticFiles(directory=settings.BASE_DIR + "/static"), name='static')

    register_router(app)

    return app


def register_router(app: FastAPI):
    app.router.include_router(router=router)
