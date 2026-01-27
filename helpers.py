import os
from getpass import getpass


def get_ionq_api_key(env_var: str = "IONQ_API_KEY") -> str:
    """Return the IonQ API key, or raise a clear error if it can't be retrieved."""
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
