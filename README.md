# Github projet

### Requirements

- Python 3
- UV

To activate venv could be done with:

```shell
source .venv/bin/activate
```


### Setup

```shell
uv pip install -r requirements.txt
```

Make sure you have `GITHUB_ACCESS_TOKEN` set in your env the env var should be like:

```shell
export GITHUB_ACCESS_TOKEN=ghp_W...
```

It should be exported in your current shell (e.g zshrc), the file path should be ~/.zshrc in this case.


### Running

```shell
python app/main.py
```

Visit - http://localhost:8000 or http://127.0.0.1:8000
You should be able to see the following message:

```shell
{"message":"Hello World from FastAPI"}
```


## Content

In this repository you could find:
* /repos - Repositories resource
* [WIP] /repos/{repo_id}/open-prs?qty=int - Pull requests resource


### Tests

The `/tests` folder is intended to contain any kind of tests code.

To run the tests use the following command:

```shell
pytest
```


### Deployment

TODO
