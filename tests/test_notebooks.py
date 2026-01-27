"""Integration tests for Jupyter notebooks.

This module executes all Jupyter notebooks in the repository to ensure they
run without errors. Tests require the IONQ_API_KEY environment variable to be
set for notebooks that make calls to IonQ's cloud APIs.
"""

import glob
import os
import subprocess
import sys

import pytest

NOTEBOOK_TIMEOUT_SECONDS = int(os.getenv("NBEXEC_TIMEOUT_SECONDS", "600"))
IONQ_API_KEY = os.getenv("IONQ_API_KEY")


def _run_notebook(path: str) -> None:
    """Execute a notebook using nbconvert and fail with useful output on error.

    Args:
        path: Path to the Jupyter notebook file to execute.

    Raises:
        AssertionError: If the notebook execution fails.
    """
    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "html",
        "--execute",
        f"--ExecutePreprocessor.timeout={NOTEBOOK_TIMEOUT_SECONDS}",
        path,
    ]
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        raise AssertionError(
            f"Error executing notebook {path}.\n\n"
            f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )


@pytest.mark.skipif(
    not IONQ_API_KEY,
    reason=(
        "IONQ_API_KEY not set; skipping notebook execution tests that call "
        "IonQ's cloud APIs."
    ),
)
def test_notebooks() -> None:
    """Execute all notebooks in the repository as an integration test.

    This test finds all .ipynb files recursively and executes them using
    jupyter nbconvert. Each notebook must complete without errors.

    Raises:
        AssertionError: If no notebooks are found or if any notebook fails.
    """
    notebooks = glob.glob("**/*.ipynb", recursive=True)
    assert notebooks, "No notebooks found to test."

    for notebook in notebooks:
        print(f"Testing {notebook}")
        _run_notebook(notebook)


if __name__ == "__main__":
    if not IONQ_API_KEY:
        print("IONQ_API_KEY not set; skipping notebook tests.")
        raise SystemExit(0)

    test_notebooks()
