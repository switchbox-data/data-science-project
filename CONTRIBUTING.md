# Contributing

Thanks for your interest in contributing! This repo contains a Copier template; contributions typically change files under `template/` or the template config `copier.yml`.

## Dev setup

```bash
uv sync --group dev
uv run pre-commit install --install-hooks
```

## Run tests

```bash
uv run pytest -q
```

## Docs

```bash
uv run mkdocs serve
```

## PR guidelines

- Keep changes minimal and Copier-native (prefer conditional paths over post-gen scripts)
- Add/adjust tests if conditionals change
- Ensure CI is green (pytest + pre-commit)
