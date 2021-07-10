from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    """Schemas for uploading url."""

    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    """Schemas for get url."""

    id: int
