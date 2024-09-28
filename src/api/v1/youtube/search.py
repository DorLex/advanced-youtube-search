from fastapi import APIRouter, Depends, Query

from src.dependencies.youtube import youtube_search
from src.schemas.youtube import ResultDataSchema, SearchQueryParamsSchema
from src.services.youtube.search import SearchService

router = APIRouter(
    prefix='/search',
    tags=['YouTube Search'],
)


@router.get('', response_model=list[ResultDataSchema])
def advanced_search(
        query_params: SearchQueryParamsSchema = Query(),
        search=Depends(youtube_search)
):
    search_results: list[ResultDataSchema] = SearchService(search).find(query_params)
    return search_results
