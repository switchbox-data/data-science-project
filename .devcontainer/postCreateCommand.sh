#!/usr/bin/env bash

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Dependencies (project + dev)
uv sync --group dev

# Install prek
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/j178/prek/releases/download/v0.2.11/prek-installer.sh | sh

# Install pre-commit hooks
prek install --install-hooks
