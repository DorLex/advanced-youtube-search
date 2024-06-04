from googleapiclient.http import HttpRequest

from src.apps.youtube_search.dependencies import CommonQueryParams, fake_response
from src.apps.youtube_search.schemas import ResultData
from src.apps.youtube_search.services.parser import SearchItemParser


class SearchService:
    def __init__(self, search):
        self._search = search
        self._Parser = SearchItemParser

    def find(self, query_params: CommonQueryParams) -> list[ResultData]:
        # response = self._get(query_params)

        response: dict = fake_response

        search_results = []
        for item in response['items']:
            parser = self._Parser(item)

            search_results.append(
                ResultData(
                    title=parser.title,
                    content_type=parser.content_type,
                    url=parser.url,
                    description=parser.description
                )
            )

        return search_results

    def _get(self, query_params: CommonQueryParams) -> dict:
        request: HttpRequest = self._search.list(
            part='snippet',
            q=query_params.q,
            type=query_params.content_type.value,
            maxResults=query_params.max_results,
            regionCode='KZ',
            relevanceLanguage=query_params.relevance_language.value
        )

        return request.execute()
