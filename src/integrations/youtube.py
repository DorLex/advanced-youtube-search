from googleapiclient.discovery import build, Resource

from src.config import settings

base_youtube_resource: Resource = build('youtube', 'v3', developerKey=settings.youtube_api_key)
