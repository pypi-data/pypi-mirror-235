#!/usr/bin/env sh

# activate .venv if available
test -d .venv/bin && . .venv/bin/activate  # Unix
test -d .venv/Scripts && .venv/Scripts/activate  # Windows

# print commands, abort on error
set -ex

black --check .
ruff check .

mypy src
mypy tests --allow-untyped-defs

pytest --cov=src --cov-config=pyproject.toml tests
