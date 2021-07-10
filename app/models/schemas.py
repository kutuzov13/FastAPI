from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    """Schemas for uploading url."""

    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    """Schemas for get url."""

    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    """Schemas for update url."""

    summary: str
