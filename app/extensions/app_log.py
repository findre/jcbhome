from loguru import logger

import os
import time
from app.core import get_settings


settings = get_settings()


log_path = os.path.join(settings.base_dir, 'logs')


if not os.path.exists(log_path):
    os.mkdir(log_path)


log_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}.log')


logger.add(
    log_path,
    level=settings,
    rotation="00:00",
    retention="2 days",
    encoding="utf-8",
    enqueue=True,
)

__all__ == ["logger"]
