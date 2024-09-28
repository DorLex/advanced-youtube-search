from fastapi import FastAPI

from src.api import api_router

app = FastAPI(
    title='Advanced YouTube Search',
    description='Расширенный поиск YouTube видео',
)

app.include_router(api_router)
