# Prompt Arguments

When running the `copier copy` command, you'll be prompted with several questions to configure your project. Here's what each option does:

---

**author**

Your full name. This will be used in documentation, license files, and package metadata.

**email**

Your email address. Used for package metadata and contact information.

**author_github_handle**

Your GitHub username or organization. This is used to set up repository URLs and documentation links.

**project_description**

A short description of your project. This appears in README files, package metadata, and documentation.

**project_features**

This is a **multiselect** option where you can choose one or more project types:

- `python_data_science`: Sets up a Python data science environment with:
  - Polars, PyArrow, Seaborn, NumPy for data analysis
  - Quarto notebooks for reproducible research
  - Modern Python tooling (uv, ruff, ty)


- `r_data_science`: Sets up an R data science environment with:
  - Tidyverse libraries (ggplot2, dplyr, etc.)
  - Quarto notebooks
  - Modern R tooling (pak, air, radian)
  - Fast package installation via P3M

- `python_package`: Creates a Python package with:
  - Build tools (hatchling)
  - Testing framework (pytest, tox)
  - Documentation (MkDocs with Material theme)
  - Publishing workflow (PyPI)

You can select multiple features! Here are some common combinations:

*Python data science project*:
```yaml
project_features: ["python_data_science"]
```

*R data science project*:
```yaml
project_features: ["r_data_science"]
```

*Polyglot data science project*:
```yaml
project_features: ["python_data_science", "r_data_science"]
```

*Python package for distribution*:
```yaml
project_features: ["python_package"]
```

*Hybrid python project (data science + package)*:
```yaml
project_features: ["python_data_science", "python_package"]
```


**use_github**

`true` or `false`. When enabled, this adds:
- GitHub Actions workflows for CI/CD
- Issue and pull request templates
- Automated testing and deployment
- Documentation publishing to GitHub Pages

**open_source_license**

Choose a license for your project. Options:
- `MIT license` - Permissive, widely used
- `BSD license` - Similar to MIT, with additional attribution requirements
- `ISC license` - Very permissive, minimal text
- `Apache Software License 2.0` - Includes patent protection
- `GNU General Public License v3` - Copyleft, requires derivative works to be open source
- `Not open source` - No license file generated

**aws**

`true` or `false`. When enabled, includes:
- AWS CLI configuration
- Boto3 for Python projects
- AWS-related development tools and examples

---

## Computed Variables

The template automatically computes several values based on your choices:

**project_name**: Automatically set to the directory name you specify when running copier

**project_slug**: Automatically generated from project_name by converting to lowercase and replacing hyphens with underscores. This is used for:
- Python package names
- Import statements: `from project_slug import module`
- Directory structures
