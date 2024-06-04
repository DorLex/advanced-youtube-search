from datetime import datetime

from src.apps.youtube_search.enums import ContentTypesEnum, UrlTemplatesEnum


class SearchItemParser:
    def __init__(self, item: dict):
        self.item = item
        self.content_type = self._get_content_type()
        self.item_id = self._get_item_id()

    def _get_content_type(self) -> str:
        kind: str = self.item['id']['kind']
        return kind.split('#')[1]

    def _get_item_id(self) -> str | None:
        if self.content_type == ContentTypesEnum.video.value:
            return self.item['id'].get('videoId')
        elif self.content_type == ContentTypesEnum.playlist.value:
            return self.item['id'].get('playlistId')
        return None

    @property
    def title(self) -> str:
        return self.item['snippet']['title']

    @property
    def published_at(self) -> str:
        published_at: str = self.item['snippet']['publishedAt']
        published_at: datetime = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
        return published_at.strftime('%d %B %Y')

    @property
    def description(self) -> str:
        return self.item['snippet']['description']

    @property
    def url(self) -> str | None:
        url_template: UrlTemplatesEnum | None = getattr(UrlTemplatesEnum, self.content_type, None)

        if self.item_id and url_template:
            return f'{url_template.value}{self.item_id}'

        return None
