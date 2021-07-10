from fastapi import APIRouter, Depends
from app.config import Setting, get_setting

router = APIRouter()


@router.get('/ping')
async def pong(settings: Setting = Depends(get_setting)):
    """Get information about the working environment."""
    return {
        'ping': 'pong!',
        'environment': settings.environment,
        'testing': settings.testing,
    }
