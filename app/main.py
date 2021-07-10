import logging

from app.api import ping, summaries
from app.db import init_db
from fastapi import FastAPI

log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    """Create application object."""
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix='/summaries', tags=['summaries'])
    return application


app = create_application()


@app.on_event('startup')
async def startup_event():
    """Connect to database when application is startup."""
    log.info('Starting up...')
    init_db(app)


@app.on_event('shutdown')
async def shutdown_event():
    """Disconnect to database when application is shutdown."""
    log.info('Shutting down...')
