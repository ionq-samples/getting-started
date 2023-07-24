import os
import nbformat
import glob
import subprocess


def test_notebook(path):
    # Run the notebook
    res = subprocess.run(
        ["python3", "-m", "nbconvert", "--to", "html", "--execute", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # If the notebook ran without errors, the return code will be 0
    if res.returncode != 0:
        raise Exception(
            f"Error executing the notebook {path}. Output:\n{res.stdout.decode('utf-8')} {res.stderr.decode('utf-8')}"
        )


def test_notebooks():
    # Get a list of all notebook files
    notebooks = glob.glob("**/*.ipynb", recursive=True)

    # Test each notebook
    for notebook in notebooks:
        print(f"Testing {notebook}")
        test_notebook(notebook)


if __name__ == "__main__":
    test_notebooks()
