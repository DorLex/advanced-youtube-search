from fastapi import Depends

from src.youtube_integration.client import youtube_service


def get_youtube():
    with youtube_service as youtube:
        yield youtube


def get_youtube_search(youtube=Depends(get_youtube)):
    return youtube.search()
