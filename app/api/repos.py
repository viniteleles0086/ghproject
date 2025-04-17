from os import environ

from agithub.GitHub import GitHub

from schemas.repo import Repo


# TODO: move it to a config file
GITHUB_ACCESS_TOKEN = environ["GITHUB_ACCESS_TOKEN"]
github_api = GitHub(token=GITHUB_ACCESS_TOKEN)


def list():
    status_code, content = github_api.repositories.get()

    return (
        status_code,
        content,
    )


def create(repo: Repo):
    repo = repo.dict()
    status_code, _content = github_api.user.repos.post(body=repo)

    return status_code


def delete(owner: str, repo: str):
    # TODO: maybe research a bit more this might be unsafe
    delete_command = f"github_api.repos.{owner}[repo].delete()"
    status_code, _content = eval(delete_command)

    return status_code
