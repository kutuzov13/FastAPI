from typing import Union, List

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
    summaries = await TextSummary.all().values()
    return summaries