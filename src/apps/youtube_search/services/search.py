from googleapiclient.http import HttpRequest

from src.apps.youtube_search.dependencies import CommonQueryParams, fake_response
from src.apps.youtube_search.enums import ContentTypesEnum, UrlTemplatesEnum
from src.apps.youtube_search.schemas import ResultData
from src.apps.youtube_search.services.parser import Parser


class SearchService:
    def __init__(self, search):
        self._search = search
        self._Parser = Parser

    def find(self, query_params: CommonQueryParams) -> list[ResultData]:
        # response = self._get(query_params)

        response: dict = fake_response

        search_results = []
        for item in response['items']:
            parser = self._Parser(item)

            content_type = parser.content_type

            if content_type == ContentTypesEnum.video.value:
                item_id = item['id'].get('videoId')
            elif content_type == ContentTypesEnum.playlist.value:
                item_id = item['id'].get('playlistId')
            else:
                item_id = ''

            url_template: str = getattr(UrlTemplatesEnum, 'content_type', UrlTemplatesEnum.youtube.value)
            url = f'{url_template}{item_id}'

            search_results.append(
                ResultData(
                    title=parser.title,
                    content_type=content_type,
                    url=url,
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
