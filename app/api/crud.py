from typing import List, Union

from app.models.schemas import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """Read the body of the request and validate data."""
    summary = TextSummary(
        url=payload.url,
        summary='dummy summary',
    )
    await summary.save()
    return summary.id


async def get(id_summer: int) -> Union[dict, None]:
    """Get summary by number id."""
    summary = await TextSummary.filter(id=id_summer).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    """Get all summaries."""
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id_summary: int) -> int:
    """Delete summary by id."""
    summary = await TextSummary.filter(id=id_summary).first().delete()
    return summary


async def put(id_summary: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    """Update summary by id."""
    summary = await TextSummary.filter(id=id_summary).update(url=payload.url, summary=payload.summary)
    if summary:
        updated_summary = await TextSummary.filter(id=id_summary).first().values()
        return updated_summary[0]
    return None
