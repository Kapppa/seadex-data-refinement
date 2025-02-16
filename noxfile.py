from __future__ import annotations

import os
import shutil
from pathlib import Path

import nox

nox.needs_version = ">=2024.10.9"
nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "build-docs"]


def install(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--locked",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )


@nox.session(venv_backend=None, default=False)
def clean(_: nox.Session) -> None:
    paths = (
        "./.mypy_cache",
        "./.pytest_cache",
        "./src/__pycache__",
        "./__pycache__",
        "./docs/build",
        "./.nox",
    )

    for p in paths:
        try:
            shutil.rmtree(p)
        except Exception:
            pass


@nox.session
def lint(session: nox.Session) -> None:
    install(session)
    if os.getenv("CI"):
        # Do not modify files in CI, simply fail.
        session.run("ruff", "check", ".")
        session.run("ruff", "format", ".", "--check")
    else:
        # Fix any fixable errors if running locally.
        session.run("ruff", "check", ".", "--fix")
        session.run("ruff", "format", ".")


@nox.session(name="build-docs")
def build_docs(session: nox.Session) -> None:
    install(session)

    src = Path.cwd() / "docs" / "source"
    build = Path.cwd() / "docs" / "build"

    session.run("sdr", "unmuxed", "--outfile", src / "unmuxed.md", *session.posargs)
    session.run("sdr", "no-comparisons", "--outfile", src / "no-comparisons.md", *session.posargs)
    session.run("sdr", "marked-incomplete", "--outfile", src / "marked-incomplete.md", *session.posargs)
    session.run("sdr", "public-non-nyaa", "--outfile", src / "public-non-nyaa.md", *session.posargs)
    session.run("sdr", "private-tracker-only", "--outfile", src / "private-tracker-only.md", *session.posargs)
    session.run("sphinx-build", "-M", "html", src, build)
