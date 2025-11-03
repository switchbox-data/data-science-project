from __future__ import annotations

import shutil
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


def _has_docker() -> bool:
    return (
        shutil.which("docker") is not None and subprocess.run(["docker", "info"], capture_output=True).returncode == 0
    )


def _has_devcontainer_cli() -> bool:
    return shutil.which("devcontainer") is not None


def test_devcontainer_ohmyzsh_plugins(tmp_path: Path) -> None:
    if not _has_docker() or not _has_devcontainer_cli():
        # Skip if local environment doesn't support container tests; covered in CI separately
        import pytest

        pytest.skip("Docker or devcontainer CLI not available")

    dest = tmp_path / "e2e"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "e2e-proj",
            "project_description": "Devcontainer E2E",
            "project_features": "[python_package]",
            "use_github": False,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr

    # Build and start the devcontainer
    up = subprocess.run(
        [
            "devcontainer",
            "up",
            "--workspace-folder",
            str(dest),
        ],
        capture_output=True,
        text=True,
    )
    assert up.returncode == 0, up.stderr

    # Verify zsh and plugins inside the container
    checks = [
        "zsh --version",
        "test -d $HOME/.oh-my-zsh",
        "grep -E 'plugins=.*zsh-autosuggestions' $HOME/.zshrc",
        "grep -E 'plugins=.*zsh-completions' $HOME/.zshrc",
        "grep -E 'plugins=.*zsh-syntax-highlighting' $HOME/.zshrc",
        "grep -E 'plugins=.*colored-man-pages' $HOME/.zshrc",
        "grep -E 'plugins=.*colorize' $HOME/.zshrc",
        "grep -E 'plugins=.*history' $HOME/.zshrc",
        "alias ll",
        "alias la",
        "alias l",
    ]
    for cmd in checks:
        r = subprocess.run(
            [
                "devcontainer",
                "exec",
                "--workspace-folder",
                str(dest),
                "zsh",
                "-lc",
                cmd,
            ],
            capture_output=True,
            text=True,
        )
        assert r.returncode == 0, f"Command failed: {cmd}\nstdout: {r.stdout}\nstderr: {r.stderr}"
