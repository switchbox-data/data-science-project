from __future__ import annotations

import subprocess
from pathlib import Path


def run_copier(template_dir: Path, dest: Path, data: dict[str, str]) -> subprocess.CompletedProcess:
    args = [
        "uvx",
        "copier",
        "copy",
        "--defaults",
        "--force",
        "--trust",
    ]
    for k, v in data.items():
        args.extend(["--data", f"{k}={v}"])
    args.extend([str(template_dir), str(dest)])
    return subprocess.run(args, check=False, capture_output=True, text=True)


def assert_exists(base: Path, *paths: str) -> None:
    for p in paths:
        assert (base / p).exists(), f"Expected to exist: {p}"


def assert_missing(base: Path, *paths: str) -> None:
    for p in paths:
        assert not (base / p).exists(), f"Expected missing: {p}"


def assert_file_contains(base: Path, file_path: str, expected_content: str) -> None:
    """Assert that a file contains expected content."""
    full_path = base / file_path
    assert full_path.exists(), f"Expected file to exist: {file_path}"
    content = full_path.read_text()
    assert expected_content in content, f"Expected '{expected_content}' in {file_path}, but got: {content}"


def test_python_data_science(tmp_path: Path) -> None:
    dest = tmp_path / "py"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "py-proj",
            "project_description": "Test py",
            "type_checker": "ty",
            "project_features": "[python_data_science]",
            "use_github": True,
            "open_source_license": "MIT license",
            "aws": True,
        },
    )
    assert res.returncode == 0, res.stderr
    assert_exists(
        dest,
        "Justfile",
        ".pre-commit-config.yaml",
        ".devcontainer",
        ".github",
        "pyproject.toml",
        "tox.ini",
        "tests",
        "py_proj",
        "notebooks",
    )


def test_python_minimal(tmp_path: Path) -> None:
    dest = tmp_path / "minimal"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "minimal-proj",
            "project_description": "Minimal Python project",
            "project_features": "[python_data_science]",
            "use_github": False,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr
    assert_exists(
        dest,
        "Justfile",
        ".pre-commit-config.yaml",
        ".devcontainer",
        "pyproject.toml",
        "tox.ini",
        "tests",
        "minimal_proj",
        "notebooks",
    )
    assert_missing(dest, ".github", "docs")


def test_no_python_features(tmp_path: Path) -> None:
    dest = tmp_path / "no-python"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "no-python-proj",
            "project_description": "Project with no Python features",
            "project_features": "[]",
            "use_github": True,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr
    assert_exists(dest, "Justfile", ".devcontainer", ".github")
    assert_missing(
        dest, ".pre-commit-config.yaml", "pyproject.toml", "tox.ini", "tests", "no_python_proj", "notebooks", "docs"
    )


def test_python_mkdocs_only(tmp_path: Path) -> None:
    dest = tmp_path / "docs"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "docs-proj",
            "project_description": "Docs only",
            "type_checker": "mypy",
            "project_features": "[python_package]",
            "use_github": True,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr
    assert_exists(
        dest, "docs", "mkdocs.yml", "pyproject.toml", "tox.ini", "docs_proj", "tests", ".github", ".devcontainer"
    )
    assert_missing(dest, "notebooks")
    # Check that postCreateCommand.sh contains the expected Python setup commands
    assert_file_contains(dest, ".devcontainer/postCreateCommand.sh", "curl -LsSf https://astral.sh/uv/install.sh | sh")
    assert_file_contains(dest, ".devcontainer/postCreateCommand.sh", "uv sync --group dev")
    assert_file_contains(dest, ".devcontainer/postCreateCommand.sh", "prek install --install-hooks")
    # Check that Justfile contains documentation commands (python_package boolean bug)
    assert_file_contains(dest, "Justfile", "# 📚 DOCUMENTATION")
    assert_file_contains(dest, "Justfile", "docs:")
    # Check that GitHub workflow contains docs check job (python_package boolean bug)
    assert_file_contains(dest, ".github/workflows/python-package-main.yml", "check-docs:")
    # Check that release workflow contains set-version job (python_package boolean bug)
    assert_file_contains(dest, ".github/workflows/on-release-main.yml", "set-version:")


def test_python_data_science_notebooks(tmp_path: Path) -> None:
    dest = tmp_path / "pydata"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "pydata-proj",
            "project_description": "Python data science project",
            "type_checker": "ty",
            "project_features": "[python_data_science]",
            "use_github": True,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr
    assert_exists(dest, "notebooks", "pyproject.toml", "tox.ini", "pydata_proj", "tests", ".github", ".devcontainer")
    assert_missing(dest, "docs", "mkdocs.yml")
    # Check that py_example.qmd contains actual content (not template condition)
    assert_file_contains(dest, "notebooks/py_example.qmd", 'title: "Python Data Analysis Example"')
    assert_file_contains(dest, "notebooks/py_example.qmd", "import polars as pl")
    # Ensure template condition is not present in final output
    content = (dest / "notebooks/py_example.qmd").read_text()
    assert '{% if cookiecutter.pydata == "y" %}' not in content, "Template condition should be resolved"


def test_project_name_in_devcontainer(tmp_path: Path) -> None:
    dest = tmp_path / "my_custom_dir"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Test",
            "email": "test@example.com",
            "author_github_handle": "test",
            "project_name": "different-name",  # This is different from directory name
            "project_features": "[python_package]",
            "use_github": True,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr
    # Check that devcontainer uses project name, not directory name
    assert_file_contains(dest, ".devcontainer/devcontainer.json", "/workspaces/different-name")
    # Should NOT contain the directory name in paths
    content = (dest / ".devcontainer/devcontainer.json").read_text()
    assert "/workspaces/my_custom_dir/" not in content
