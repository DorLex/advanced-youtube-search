from datetime import date

from pydantic import BaseModel, HttpUrl, Field

from src.apps.youtube_search.enums import ContentTypesEnum, RelevanceLanguagesEnum


class SearchQueryParamsSchema(BaseModel):
    q: str = Field(description='Поисковый запрос')
    content_type: ContentTypesEnum = Field(description='Тип')
    relevance_language: RelevanceLanguagesEnum = Field(description='Язык')
    max_results: int = Field(5, ge=0, le=50, description='Количество')
    after: date = Field(None, description='После даты. (Например: 2024-05-01)')
    before: date = Field(None, description='До даты. (Например: 2024-06-01)')


class ResultDataSchema(BaseModel):
    title: str
    channel_title: str
    content_type: str
    published_at: str
    url: HttpUrl | None
    description: str
