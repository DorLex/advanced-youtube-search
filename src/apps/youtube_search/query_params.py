# from dataclasses import dataclass
# from datetime import date
#
# from fastapi import Query
#
# from src.apps.youtube_search.enums import ContentTypesEnum, RelevanceLanguagesEnum
#
#
# @dataclass
# class CommonQueryParams:
#     q: str = Query(description='Поисковый запрос')
#     content_type: ContentTypesEnum = Query(description='Тип')
#     relevance_language: RelevanceLanguagesEnum = Query(description='Язык')
#     max_results: int = Query(5, ge=0, le=50, description='Количество')
#     after: date = Query(None, description='После даты. (Например: 2024-05-01)')
#     before: date = Query(None, description='До даты. (Например: 2024-06-01)')
