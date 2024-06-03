from fastapi import FastAPI

from src.apps.youtube_search.routers.local_router import youtube_router

app = FastAPI(
    title='Advanced YouTube Search',
    description='Расширенный поиск YouTube видео',
)

app.include_router(youtube_router)
