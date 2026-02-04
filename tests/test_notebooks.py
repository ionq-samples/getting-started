"""Integration tests for Jupyter notebooks.

This module executes all Jupyter notebooks in the repository to ensure they
run without errors. Tests require the IONQ_API_KEY environment variable to be
set for notebooks that make calls to IonQ's cloud APIs.

Logging is configured to output to console with INFO level by default.
Configure logging level via LOGLEVEL environment variable if needed.
"""

import glob
import logging
import os
import subprocess
import sys
import time

import pytest

from tests.constants import (
    DEFAULT_TIMEOUT_SECONDS,
    ENV_API_KEY,
    ENV_TIMEOUT,
    SEPARATOR_WIDTH,
)

# Configure logging
logging.basicConfig(
    level=os.getenv("LOGLEVEL", "INFO"),
    format="%(message)s",
)
logger = logging.getLogger(__name__)

# Load configuration from environment
NOTEBOOK_TIMEOUT_SECONDS = int(os.getenv(ENV_TIMEOUT, str(DEFAULT_TIMEOUT_SECONDS)))
IONQ_API_KEY = os.getenv(ENV_API_KEY)


def _print_section(title: str, char: str = "=") -> None:
    """Print a formatted section header.

    Args:
        title: The title text to display.
        char: Character to use for the separator line (default "=").
    """
    logger.info("")
    logger.info(char * SEPARATOR_WIDTH)
    logger.info(title)
    logger.info(char * SEPARATOR_WIDTH)


def _run_notebook(path: str) -> None:
    """Execute a notebook using nbconvert and fail with useful output on error.

    Args:
        path: Path to the Jupyter notebook file to execute.

    Raises:
        AssertionError: If the notebook execution fails.
    """
    _print_section(f"Executing: {path}")
    logger.info(f"Timeout: {NOTEBOOK_TIMEOUT_SECONDS}s")

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

    logger.info(f"Running command: {' '.join(cmd)}")
    logger.info(f"Starting execution at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    elapsed_time = time.time() - start_time

    if result.returncode != 0:
        logger.error(f"✗ FAILED after {elapsed_time:.2f}s")
        logger.error(f"\nSTDOUT:\n{result.stdout}")
        logger.error(f"\nSTDERR:\n{result.stderr}")
        raise AssertionError(
            f"Error executing notebook {path} after {elapsed_time:.2f}s.\n\n"
            f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    logger.info(f"✓ PASSED in {elapsed_time:.2f}s")
    logger.info(f"Completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")


def _discover_notebooks() -> list[str]:
    """Discover all notebook files, excluding venv.

    Returns:
        A sorted list of notebook file paths.
    """
    notebooks = sorted(glob.glob("**/*.ipynb", recursive=True))
    # Exclude notebooks in venv directory
    return [nb for nb in notebooks if "venv/" not in nb and "/.venv/" not in nb]


# Discover notebooks at module load time for pytest parametrization
NOTEBOOKS = _discover_notebooks()


@pytest.mark.skipif(
    not IONQ_API_KEY,
    reason=(
        f"{ENV_API_KEY} not set; skipping notebook execution tests that call "
        "IonQ's cloud APIs."
    ),
)
@pytest.mark.parametrize("notebook_path", NOTEBOOKS)
def test_notebook_execution(notebook_path: str) -> None:
    """Execute a single notebook as an integration test.

    This test executes a Jupyter notebook using jupyter nbconvert and fails
    if the notebook execution encounters any errors.

    Args:
        notebook_path: Path to the notebook file to execute.

    Raises:
        AssertionError: If the notebook execution fails.
    """
    _run_notebook(notebook_path)


if __name__ == "__main__":
    _print_section("Notebook Integration Test Runner")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Timeout per notebook: {NOTEBOOK_TIMEOUT_SECONDS}s")
    logger.info(f"API Key configured: {'Yes' if IONQ_API_KEY else 'No'}")
    logger.info("")

    if not IONQ_API_KEY:
        logger.warning(f"⚠ {ENV_API_KEY} not set; skipping notebook tests.")
        raise SystemExit(0)

    # When running as script, execute all notebooks manually
    _print_section(f"Found {len(NOTEBOOKS)} notebook(s) to test")
    for i, nb in enumerate(NOTEBOOKS, 1):
        logger.info(f"{i}. {nb}")

    assert NOTEBOOKS, "No notebooks found to test."

    total_start = time.time()
    passed = 0
    failed = 0

    for notebook in NOTEBOOKS:
        try:
            _run_notebook(notebook)
            passed += 1
        except AssertionError:
            failed += 1
            logger.error(f"Notebook {notebook} failed, continuing with remaining tests")

    total_elapsed = time.time() - total_start

    _print_section("Test Summary")
    logger.info(f"Total notebooks: {len(NOTEBOOKS)}")
    logger.info(f"✓ Passed: {passed}")
    logger.info(f"✗ Failed: {failed}")
    logger.info(f"Total time: {total_elapsed:.2f}s")
    logger.info("")

    if failed > 0:
        raise SystemExit(f"{failed} notebook(s) failed to execute")
