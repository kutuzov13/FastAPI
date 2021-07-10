from typing import List

from app.api import crud
from app.models.schemas import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema
from fastapi import APIRouter, HTTPException, Path

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
async def read_summary(id_summary: int = Path(..., gt=0)) -> SummarySchema:
    """Get summary by number id."""
    summary = await crud.get(id_summary)
    if not summary:
        raise HTTPException(status_code=NOT_FOUND_CODE, detail='Summary not found')
    return summary


@router.get('/', response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    """Get all summary."""
    return await crud.get_all()


@router.delete('/{id}/', response_model=SummaryResponseSchema)
async def delete_summary(id_summary: int = Path(..., gt=0)) -> SummaryResponseSchema:
    """Handel delete summary."""
    summary = await crud.get(id_summary)
    if not summary:
        raise HTTPException(status_code=404, detail='Summary not found')
    await crud.delete(id_summary)
    return summary


@router.put('/{id}/', response_model=SummarySchema)
async def update_summary(payload: SummaryUpdatePayloadSchema, id_summary: int = Path(..., gt=0)) -> SummarySchema:
    """Handel update summary."""
    summary = await crud.put(id_summary, payload)
    if not summary:
        raise HTTPException(status_code=404, detail='Summary not found')
    return summary
