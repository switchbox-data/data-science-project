# Switchbox Copier Template

This is a standalone Copier template for Switchbox projects. It supports:

- Python-focused development with modern tooling
- Optional features: Data science tools, package publishing, GitHub Actions, AWS CLI
- Python stack options: type checker (mypy/ty), always includes deptry and devcontainers
- Conditional files and directories via Copier-native templated paths, no post-gen cleanup

## Quick start

Install Copier:

```bash
pipx install copier  # or: uv tool install copier
```

Generate a project (example: Python + Data Science tools):

```bash
copier copy --defaults --force \
  --data python_data_science="y" --data python_package="y" \
  . /path/to/new-project
```

See `copier/copier.yml` for all questions and defaults.

## Development

- Install dev deps with uv:

```bash
uv sync --group dev
```

- Run tests (pytest runs copier to generate scenarios and asserts outputs):

```bash
uv run pytest -q
```

- Lint/format:

```bash
uv run pre-commit run -a
```

## Docs

This repo ships MkDocs. To serve locally:

```bash
uv run mkdocs serve
```

## Using the Template

To create a new project from this template:

```bash
# Install copier
uv tool install copier

# Create a new project (requires --trust for git initialization)
copier copy --trust https://github.com/your-org/copier-sb.git my-new-project
```

The template will:
- 🔧 Initialize a git repository
- 📁 Add all generated files to git
- 💾 Create an initial commit
- 🚀 Set up your development environment

### Project Types

You can select one or more of these project types:
- **Python Data Science**: Includes polars, pyarrow, seaborn, numpy, Quarto notebooks
- **Python Package**: Includes build tools, twine, MkDocs documentation
- **R Data Science**: Includes R, renv, Quarto, R extensions

**Note**: You must select at least one project type.

## License

MIT
