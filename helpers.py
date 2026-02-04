"""Utility functions for IonQ getting-started notebooks.

This module provides helper functions for common tasks across Jupyter notebooks,
such as retrieving API keys from environment variables with fallback to
interactive prompts.

Example:
    from helpers import get_ionq_api_key

    # Retrieve API key (checks IONQ_API_KEY env var, then prompts)
    api_key = get_ionq_api_key()

    # Or use a custom environment variable name
    api_key = get_ionq_api_key("MY_CUSTOM_API_KEY")
"""

import os
from getpass import getpass


def get_ionq_api_key(env_var: str = "IONQ_API_KEY") -> str:
    """Return the IonQ API key, or raise a clear error if it can't be retrieved.

    This function first checks the specified environment variable. If not found,
    it attempts to prompt the user interactively using getpass for secure input.

    Args:
        env_var: Name of the environment variable containing the API key.
            Defaults to "IONQ_API_KEY".

    Returns:
        The IonQ API key as a string.

    Raises:
        RuntimeError: If the environment variable is not set and interactive
            input is not available (e.g., in non-TTY environments).

    Example:
        >>> api_key = get_ionq_api_key()  # Checks IONQ_API_KEY
        >>> api_key = get_ionq_api_key("CUSTOM_KEY")  # Checks CUSTOM_KEY
    """
    api_key = os.getenv(env_var)
    if api_key:
        return api_key

    try:
        return getpass(f"Enter your IonQ API key ({env_var}): ")
    except (EOFError, KeyboardInterrupt) as exc:
        raise RuntimeError(
            f"No {env_var} environment variable is set and an interactive prompt "
            "isn't available. Please set your IonQ API key before running this notebook."
        ) from exc
