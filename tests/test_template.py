from __future__ import annotations

import subprocess
from pathlib import Path


def run_copier(template_dir: Path, dest: Path, data: dict[str, str]) -> subprocess.CompletedProcess:
    args = [
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
