from fastapi import Depends
from googleapiclient.discovery import Resource

from src.integrations.youtube import base_youtube_resource


def youtube_resource() -> Resource:
    with base_youtube_resource as youtube:
        yield youtube


def youtube_search(youtube=Depends(youtube_resource)) -> Resource:
    return youtube.search()
