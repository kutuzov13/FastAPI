from typing import List

from app.api import crud
from app.models.schemas import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

CREATE_CODE = 201
NOT_FOUND_CODE = 404


@router.post('/', response_model=SummaryResponseSchema, status_code=CREATE_CODE)
async def create_summary(payload: SummaryPayloadSchema):
    """Create summary."""
    summary_id = await crud.post(payload)

    response_object = {
        'id': summary_id,
        'url': payload.url,
    }
    return response_object


@router.get('/{id}/', response_model=SummarySchema)
async def read_summary(id_summer: int) -> SummarySchema:
    """Get summary by number id."""
    summary = await crud.get(id_summer)
    if not summary:
        raise HTTPException(status_code=NOT_FOUND_CODE, detail='Summary not found')
    return summary


@router.get('/', response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    """Get all summary."""
    return await crud.get_all()
