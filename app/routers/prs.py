from fastapi import APIRouter
from fastapi.responses import JSONResponse

# from app.api import api


router = APIRouter(
    prefix="/repos/{repo_id}/open-prs",
    tags=["prs"],
    responses={
        404: {"description": "Not found"},
        400: {"description": "Bad request"},
    },
)


@router.get("/")
async def list_open_prs(qty: str | None = None):
    """
    Repositories list the N pull requests open and
    the name of the contributors on the PR
    """

    qty = _get_qty_parsed(qty)
    if qty == ValueError:
        return JSONResponse(
            status_code=400,
            content={"message": "Quantity needs to be a number"}
        )

    return [{"pr": "prex"}]


def _get_qty_parsed(qty):
    if qty:
        try:
            return int(qty)
        except ValueError:
            return ValueError

    return None
