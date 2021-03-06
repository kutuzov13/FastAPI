import logging
import os
import types

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger('uvicorn')


TORTOISE_ORM = types.MappingProxyType({
    'connections': {'default': os.getenv('DATABASE_URL')},
    'apps': {
        'models': {
            'models': ['app.models.tortoise', 'aerich.models'],
            'default_connection': 'default',
        },
    },
})


def init_db(app: FastAPI) -> None:
    """Init database via Tortoise ORM."""
    Tortoise.init_models(['app.models.tortoise'], 'models')
    register_tortoise(
        app,
        db_url=os.getenv('DATABASE_URL'),
        modules={'models': ['app.models.tortoise']},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """Generate database schema via Tortoise."""
    log.info('Initializing Tortoise...')

    await Tortoise.init(
        db_url=os.getenv('DATABASE_URL'),
        modules={'models': ['app.models.tortoise']},
    )
    log.info('Generating database schema via Tortoise...')
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()

if __name__ == '__main__':
    run_async(generate_schema())
