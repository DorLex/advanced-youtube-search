from fastapi import APIRouter, Depends

from src.apps.youtube_search.dependencies import get_youtube_search
from src.apps.youtube_search.query_params import CommonQueryParams
from src.apps.youtube_search.schemas import ResultData
from src.apps.youtube_search.services.search import SearchService

router = APIRouter(
    prefix='/search',
    tags=['YouTube Search'],
)


@router.get('/', response_model=list[ResultData])
def youtube_search(
        query_params: CommonQueryParams = Depends(CommonQueryParams),
        search=Depends(get_youtube_search)
):
    search_results: list[ResultData] = SearchService(search).find(query_params)
    return search_results
