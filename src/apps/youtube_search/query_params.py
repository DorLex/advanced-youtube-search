from datetime import date

from fastapi import Query

from src.apps.youtube_search.enums import ContentTypesEnum, RelevanceLanguagesEnum


class CommonQueryParams:
    def __init__(
            self,
            q: str = Query(description='Поисковый запрос'),
            content_type: ContentTypesEnum = Query(description='Тип'),
            relevance_language: RelevanceLanguagesEnum = Query(description='Язык'),
            max_results: int = Query(5, ge=0, le=50, description='Количество'),
            after: date = Query(None, description='После даты. (Например: 2024-05-01)'),
            before: date = Query(None, description='До даты. (Например: 2024-06-01)'),
    ):
        self.q = q
        self.content_type = content_type
        self.relevance_language = relevance_language
        self.max_results = max_results
        self.after = after
        self.before = before
