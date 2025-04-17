from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from api import repos

from schemas.repo import Repo


router = APIRouter(
    prefix="/repos",
    tags=["repos"],
    responses={
        404: {"description": "Not found"},
        400: {"description": "Bad request"},
        401: {"description": "Bad credentials"},
        422: {"description": "Unprocessable Entity"},
    },
)


@router.get("/")
async def list_repos():
    """
    List github repositories
    """

    status_code, repos_ = repos.list()
    return JSONResponse(status_code=status_code, content=repos_,)


@router.post("/")
async def create_repo(repo: Repo):
    """
    Create github repository
    """

    status_code = repos.create(repo)
    return JSONResponse(status_code=status_code, content=None,)


@router.delete("/{owner}/{repo}")
async def delete_repo(owner: str, repo: str):
    """
    Delete github repository
    """

    status_code = repos.delete(owner, repo)
    return Response(status_code=status_code,)
