from fastapi import APIRouter
from src.api.v1.youtube import search

youtube_router = APIRouter(
    prefix='/youtube',
)

youtube_router.include_router(search.router)
