from googleapiclient.discovery import build

from src.config import settings

youtube_service = build('youtube', 'v3', developerKey=settings.youtube_api_key)
