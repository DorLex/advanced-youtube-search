from pydantic import BaseModel, HttpUrl


class ResultData(BaseModel):
    title: str
    channel_title: str
    content_type: str
    published_at: str
    url: HttpUrl | None
    description: str
