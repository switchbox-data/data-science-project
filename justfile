set shell := ["/bin/bash", "-c"]

setup:
    uv sync --group dev
    uv run pre-commit install --install-hooks

test:
    uv run pytest -q

lint:
    uv run pre-commit run -a

format:
    uv run ruff format .

docs:
    uv run mkdocs build -s

docs-serve:
    uv run mkdocs serve

generate *args:
    ./copier-helper.sh {{args}}

clean:
    rm -rf .pytest_cache .ruff_cache site dist build tmp
