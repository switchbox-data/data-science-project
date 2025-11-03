from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


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


devcontainer_cli = shutil.which("devcontainer")


@pytest.mark.skipif(not devcontainer_cli, reason="devcontainer CLI not installed")
def test_devcontainer_tools_and_aliases(tmp_path: Path) -> None:
    dest = tmp_path / "container-proj"
    res = run_copier(
        Path(__file__).parents[1],
        dest,
        {
            "author": "Switchbox",
            "email": "hello@switch.box",
            "author_github_handle": "switchbox-data",
            "project_name": "container-proj",
            "project_description": "Container test",
            "project_features": "[]",
            "use_github": False,
            "open_source_license": "MIT license",
            "aws": False,
        },
    )
    assert res.returncode == 0, res.stderr

    # Build the devcontainer
    build = subprocess.run(
        ["devcontainer", "build", "--workspace-folder", str(dest)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert build.returncode == 0, build.stderr

    # Verify tools exist
    for cmd in [
        "command -v eza",
        "command -v ag",
        # fd binary name differs on Debian/Ubuntu
        "(command -v fd || command -v fdfind)",
        "command -v bat",
    ]:
        proc = subprocess.run(
            [
                "devcontainer",
                "exec",
                "--workspace-folder",
                str(dest),
                "bash",
                "-lc",
                cmd,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        assert proc.returncode == 0, f"Command not found in container: {cmd}\nSTDERR: {proc.stderr}"

    # Verify aliases are set for ls and grep
    for alias_cmd, expected in [("alias ls", "eza"), ("alias grep", "ag")]:
        proc = subprocess.run(
            [
                "devcontainer",
                "exec",
                "--workspace-folder",
                str(dest),
                "bash",
                "-lc",
                alias_cmd,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        assert proc.returncode == 0, proc.stderr
        assert expected in proc.stdout, f"Expected alias output to contain {expected}, got: {proc.stdout}"
