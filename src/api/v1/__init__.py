from fastapi import APIRouter

from src.api.v1.youtube import youtube_router

v1_router = APIRouter(
    prefix='/v1',
)

v1_router.include_router(youtube_router)
