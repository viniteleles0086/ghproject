from fastapi import FastAPI

from routers import repos, prs


app = FastAPI()
app.include_router(repos.router)
app.include_router(prs.router)


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}
