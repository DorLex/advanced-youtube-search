from pydantic import BaseModel, HttpUrl


class ResultData(BaseModel):
    title: str
    content_type: str
    url: HttpUrl | None
    description: str
