# Switchbox Copier Template

This is a standalone Copier template for Switchbox projects. It supports:

- Python-focused development with modern tooling
- Optional features: Data science tools, package publishing, GitHub Actions, AWS CLI
- Python stack options: type checker (mypy/ty), always includes deptry and devcontainers
- Conditional files and directories via Copier-native templated paths, no post-gen cleanup

## Using the Template

To create a new project from this template:

```bash
# Install copier
uv tool install copier # or use pipx

# Create a new project (requires --trust for git initialization)
copier copy --trust https://github.com/your-org/copier-sb.git path/to/my-new-project
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
  https://github.com/your-org/copier-sb.git /path/to/new-project
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
