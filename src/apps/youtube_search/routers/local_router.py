from fastapi import APIRouter

from src.apps.youtube_search.routers.search import router as search_router

youtube_router = APIRouter(
    prefix='/youtube',
)

youtube_router.include_router(search_router)
