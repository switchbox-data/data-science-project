#!/usr/bin/env bash

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Dependencies (project + dev)
uv sync --group dev

# Install pre-commit hooks
uv run pre-commit install --install-hooks
