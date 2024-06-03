from fastapi import APIRouter, Depends
from googleapiclient.http import HttpRequest

from src.apps.youtube_search.dependencies import get_youtube_search

router = APIRouter(
    prefix='/search',
    tags=['YouTube Search'],
)


@router.get('/video/')
def video_search(search=Depends(get_youtube_search)):
    request: HttpRequest = search.list(
        part='snippet',
        q='fastapi',
        type='video',
        maxResults=1,
        regionCode='KZ',
        relevanceLanguage='en'
    )

    response: dict = request.execute()

    return response


@router.get('/playlist/')
def playlist_search():
    return {'msg': 'playlist_search'}
