# Switchbox Copier Template

This Coper template lets you bootstrap python packages or polyglot data science projects. 

For python packages, it supports:
- Modern python tooling: uv, ruff, ty, pytest, tox
- Package building and publishing with hatchling
- MkDocs documentation with Material theme

For python data science projects, it supports:
- Pydata libraries: polars, pyarrow, seaborn
- Quarto notebooks
- Modern python tooling: uv, ruff, ty

For R data science projects, it supports:
- Tidyverse libaries: ggplot, dplyr, etc.
- Quarto notebooks
- Modern R tooling: pak, air, radian
- Fast install of compiled R packages via pak and P3M 
- VS Code extensions for R

All project types include:
- just for task automation and project management
- devcontainers for consistent development environments
- pre-commit hooks for automated code quality checks
- Optional AWS integration (boto3 for Python, AWS CLI for all)
- Optional GitHub Actions workflows for CI/CD

## Using the Template

To create a new project from this template:

```bash
# Install copier
uv tool install copier # or use pipx

# Create a new project (requires --trust for git initialization)
copier copy --trust https://github.com/switchbox-data/data-science-project.git path/to/my-new-project
```

You'll be asked a series of questions to customize your project, including whether you use Github or AWS, and the type of project you want to make:

- **Python Data Science**: Includes polars, pyarrow, seaborn, numpy, Quarto notebooks
- **R Data Science**: Includes R, renv, Quarto, R extensions
- **Python Package**: Includes build tools, twine, MkDocs documentation

You can select one or more of these project types! They are discrete modules that compose neatly. And you can come back and add a module later.

After making your selections, copier will:
- 🔧 Initialize a git repository
- 📁 Add all generated files to git
- 💾 Create an initial commit
- 🚀 Set up your development environment

## Using the CLI

If you want to skip copier's interactive prompts and generate the project directly, you can pass arguments directly.

For instance, the following prompt generates a python package + data science project: 

```bash
copier copy --defaults --force \
  --data project_features='["python_data_science","python_package"]' \
  https://github.com/switchbox-data/data-science-project.git /path/to/new-project
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

- Serving the docs locally

```bash
uv run mkdocs serve
```



## License

MIT
