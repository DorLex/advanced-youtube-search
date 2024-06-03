from fastapi import Depends, Query

from src.apps.youtube_search.enums import ContentTypesEnum, RelevanceLanguagesEnum
from src.youtube_integration.client import youtube_service


def get_youtube():
    with youtube_service as youtube:
        yield youtube


def get_youtube_search(youtube=Depends(get_youtube)):
    return youtube.search()


class CommonQueryParams:
    def __init__(
            self,
            q: str = Query(description='Поисковый запрос'),
            content_type: ContentTypesEnum = Query(description='Тип'),
            relevance_language: RelevanceLanguagesEnum = Query(description='Язык'),
            max_results: int = Query(5, ge=0, le=50, description='Количество')
    ):
        self.q = q
        self.content_type = content_type
        self.relevance_language = relevance_language
        self.max_results = max_results


fake_response = {
    "kind": "youtube#searchListResponse",
    "etag": "p0E0D3yV8LVGYLlPQp-tJu4czr0",
    "nextPageToken": "CAIQAA",
    "regionCode": "KZ",
    "pageInfo": {
        "totalResults": 501073,
        "resultsPerPage": 2
    },
    "items": [
        {
            "kind": "youtube#searchResult",
            "etag": "dG6HXDCj8QNl4fLn3ZfLFX11M_8",
            "id": {
                "kind": "youtube#playlist",
                "playlistId": "PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS"
            },
            "snippet": {
                "publishedAt": "2022-11-20T19:07:34Z",
                "channelId": "UC5C088kVlcF5ras7cBbdWxw",
                "title": "FastAPI Курс",
                "description": "Мой расширенный курс по backend разработке на FastAPI для тех, кто хочет быстро сменить стек или найти работу: ...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/gBfkX9H3szQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/gBfkX9H3szQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/gBfkX9H3szQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "Артём Шумейко",
                "liveBroadcastContent": "none",
                "publishTime": "2022-11-20T19:07:34Z"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "p1sTW-xSM4QWdTOKSIEVL4fSDKE",
            "id": {
                "kind": "youtube#video",
                "videoId": "x4NyVVPuOR8"
            },
            "snippet": {
                "publishedAt": "2024-05-24T10:00:06Z",
                "channelId": "UC5C088kVlcF5ras7cBbdWxw",
                "title": "9 причин учить FastAPI в 2024 — Лучший фреймворк на Python?",
                "description": "9 причин, почему FastAPI сейчас — лучший выбор для Python Backend разработчика. Погружение в Backend разработку на ...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/x4NyVVPuOR8/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/x4NyVVPuOR8/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/x4NyVVPuOR8/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "Артём Шумейко",
                "liveBroadcastContent": "none",
                "publishTime": "2024-05-24T10:00:06Z"
            }
        }
    ]
}
