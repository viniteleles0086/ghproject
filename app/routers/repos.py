from fastapi import APIRouter

# from app.api import api


router = APIRouter(
    prefix="/repos",
    tags=["repos"],
    responses={
        404: {"description": "Not found"},
        400: {"description": "Bad request"},
    },
)


@router.get("/")
async def list_repos():
    """
    List github repositories
    """

    return [{"repo": "ex"}]


@router.post("/")
async def create_repo():
    """
    Create github repository
    """

    return {"repo": "ex"}


@router.delete("/{repo_id}")
async def delete_repo(repo_id: str):
    """
    Delete github repository
    """

    return {"repo": repo_id}
