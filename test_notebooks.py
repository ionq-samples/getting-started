import os
import subprocess
import nbformat
import glob


def test_notebook(path):
    # Reading the notebook
    nb = nbformat.read(path, as_version=4)

    proc = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--ExecutePreprocessor.kernel_name=python3",
            "--ExecutePreprocessor.timeout=60",
            "--output",
            "/dev/null",
            path,
        ],
        capture_output=True,
    )
    # return the result of the subprocess instead of asserting
    return proc


def test_notebooks():
    for notebook in glob.glob("**/*.ipynb", recursive=True):
        yield notebook


def main():
    for notebook in test_notebooks():
        result = test_notebook(notebook)
        if result.returncode != 0:
            print(f"The notebook {notebook} failed with the following error:\n")
            # print the stdout and stderr if the notebook failed to execute
            print(result.stdout.decode())
            print(result.stderr.decode())


if __name__ == "__main__":
    main()
