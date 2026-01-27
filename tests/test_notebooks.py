"""Integration tests for Jupyter notebooks.

This module executes all Jupyter notebooks in the repository to ensure they
run without errors. Tests require the IONQ_API_KEY environment variable to be
set for notebooks that make calls to IonQ's cloud APIs.
"""

import glob
import os
import subprocess
import sys
import time

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
    print(f"\n{'='*60}")
    print(f"Executing: {path}")
    print(f"Timeout: {NOTEBOOK_TIMEOUT_SECONDS}s")
    print(f"{'='*60}")

    start_time = time.time()

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

    print(f"Running command: {' '.join(cmd)}")
    print(f"Starting execution at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    elapsed_time = time.time() - start_time

    if result.returncode != 0:
        print(f"✗ FAILED after {elapsed_time:.2f}s")
        print(f"\nSTDOUT:\n{result.stdout}")
        print(f"\nSTDERR:\n{result.stderr}")
        raise AssertionError(
            f"Error executing notebook {path} after {elapsed_time:.2f}s.\n\n"
            f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    print(f"✓ PASSED in {elapsed_time:.2f}s")
    print(f"Completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")


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
    notebooks = sorted(glob.glob("**/*.ipynb", recursive=True))

    print(f"\n{'='*60}")
    print(f"Found {len(notebooks)} notebook(s) to test")
    print(f"{'='*60}")
    for i, nb in enumerate(notebooks, 1):
        print(f"{i}. {nb}")

    assert notebooks, "No notebooks found to test."

    total_start = time.time()
    passed = 0
    failed = 0

    for notebook in notebooks:
        try:
            _run_notebook(notebook)
            passed += 1
        except AssertionError as e:
            failed += 1
            if not os.getenv("PYTEST_CURRENT_TEST"):
                # Only re-raise if not running under pytest
                raise

    total_elapsed = time.time() - total_start

    print(f"\n{'='*60}")
    print(f"Test Summary")
    print(f"{'='*60}")
    print(f"Total notebooks: {len(notebooks)}")
    print(f"✓ Passed: {passed}")
    print(f"✗ Failed: {failed}")
    print(f"Total time: {total_elapsed:.2f}s")
    print(f"{'='*60}\n")

    if failed > 0:
        raise AssertionError(f"{failed} notebook(s) failed to execute")


if __name__ == "__main__":
    print(f"\n{'='*60}")
    print(f"Notebook Integration Test Runner")
    print(f"{'='*60}")
    print(f"Python version: {sys.version}")
    print(f"Timeout per notebook: {NOTEBOOK_TIMEOUT_SECONDS}s")
    print(f"API Key configured: {'Yes' if IONQ_API_KEY else 'No'}")
    print(f"{'='*60}\n")

    if not IONQ_API_KEY:
        print("⚠ IONQ_API_KEY not set; skipping notebook tests.")
        raise SystemExit(0)

    test_notebooks()
