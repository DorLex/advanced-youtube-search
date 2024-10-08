from googleapiclient.http import HttpRequest

from src.schemas.youtube import ResultDataSchema, SearchQueryParamsSchema
from src.services.youtube.parser import SearchItemParser


class SearchService:
    def __init__(self, search):
        self._search = search
        self._Parser = SearchItemParser

    def find(self, query_params: SearchQueryParamsSchema) -> list[ResultDataSchema]:
        response = self._get(query_params)

        search_results = []
        for item in response['items']:
            parser = self._Parser(item)

            search_results.append(
                ResultDataSchema(
                    title=parser.title,
                    channel_title=parser.channel_title,
                    content_type=parser.content_type,
                    published_at=parser.published_at,
                    url=parser.url,
                    description=parser.description
                )
            )

        return search_results

    def _get(self, query_params: SearchQueryParamsSchema) -> dict:
        search_query = self._generate_search_query(query_params)

        request: HttpRequest = self._search.list(
            part='snippet',
            q=search_query,
            type=query_params.content_type.value,
            maxResults=query_params.max_results,
            regionCode='KZ',
            relevanceLanguage=query_params.relevance_language.value
        )

        return request.execute()

    def _generate_search_query(self, query_params: SearchQueryParamsSchema) -> str:
        search_query: str = query_params.q

        if query_params.after:
            search_query += f' after:{query_params.after}'
        if query_params.before:
            search_query += f' before:{query_params.before}'

        return search_query
