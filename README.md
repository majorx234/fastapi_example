# Info

## Setup:
- `uv venv --python 3.13 env`
- `source env/bin/activate`
- `uv pip install -e .`

## Run:
- `python webserver/main.py`

## Tes:
- `curl --request GET http://127.0.0.1:8000/user/get_users`
