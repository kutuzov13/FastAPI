import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger('uvicorn')


class Setting(BaseSettings):
    """Check defines the environment."""

    environment: str = os.getenv('ENVIRONMENT')
    testing: bool = os.getenv('TESTING')
    database_url: AnyUrl = os.getenv('DATABASE_URL')


@lru_cache()
def get_setting() -> BaseSettings:
    """Get Base Settings and append in cache."""
    log.info('Loading config settings from the environment...')
    return Setting()
