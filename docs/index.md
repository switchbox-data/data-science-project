# Switchbox Copier Template

This is a modern [copier](https://copier.readthedocs.io/en/stable/) template you can use to create python and R data science projects, using modern tools, including [devcontainers](https://containers.dev/).

It supports the following features:

### Python data science
- PyData packages: [polars](https://pola.rs/), [seaborn](https://seaborn.pydata.org/)
- [Quarto](https://quarto.org/) notebooks
- [uv](https://docs.astral.sh/uv/) for dependency management
- [ruff](https://docs.astral.sh/ruff/) for code linting and formatting
- [ty](https://docs.astral.sh/ty/) for type checking

### R data science
- Tidyverse packages: [dplyr](https://dplyr.tidyverse.org/), [ggplot2](https://ggplot2.tidyverse.org/), etc.
- [Quarto](https://quarto.org/) notebooks
- [pak](TK) for dependency management
- [air](https://posit-dev.github.io/air/) for code formatting
- [radian](https://github.com/randy3k/radian) for R console
- Fast install of binary packages via [P3M](https://packagemanager.posit.co/__docs__/admin/serving-binaries.html)

### Python packages
- Modern python tooling: uv, ruff, ty, pytest, tox
- [hatchling](https://pypi.org/project/hatchling/) for package building
- [twine](https://twine.readthedocs.io/en/stable/) for package publishing
- MkDocs documentation with Material theme

### All projects

- [just](https://just.systems/man/en/) for task automation and project management
- [devcontainers](https://containers.dev/) for consistent development environments in VSCode, Cursor, Positron, and other IDEs
- [prek](https://prek.j178.dev/) for fast pre-commit hooks that automate code quality checks
- AWS integration (Optional): ([aws cli](https://aws.amazon.com/cli/), [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for Python)
- GitHub Actions Workflows (Optional): to run code quality checks and tests via CI/CD


## Quickstart

First, make sure you have copier installed. We recommend doing this with uv or pipx:

```bash
uv tool install copier # or: pipx install copier
```

On your local machine, navigate to the directory in which you want to create your project, and run the following command:

```bash
copier copy https://github.com/switchbox-data/switchbox-copier-template <my-project>
```

Where `<my-project>` is the name you want to give your project. This will be used as the directory name, and as the name of your repo if you use GitHub. 

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

## Acknowledgements

This project is inspired by the [cookiecutter-uv](https://fpgmaas.github.io/cookiecutter-uv/) package.