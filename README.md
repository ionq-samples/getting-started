# IonQ Quantum Computing Samples

This repository contains Python samples exploring quantum computing on IonQ's platform using various quantum programming libraries. These examples are a great place to start if you're interested in quantum computation, but aren't familiar with any of the libraries out there.

If you're looking for advanced and in-depth examples for a given library that implement a specific algorithm, check out some of the other projects in the [ionq-samples](https://github.com/ionq-samples) organization on GitHub.

---

## Prerequisites

There are a wide variety of ways to run these notebooks, but for starters you'll need:

1. [Python](https://www.python.org/downloads/) installed, using a version between 3.8 and 3.11.
2. A [virtual environment](https://docs.python.org/3/library/venv.html) to help ensure your dependencies don't conflict with anything else you have installed.
3. An [IonQ API key](https://cloud.ionq.com/settings/keys), which optionally you can store as an environment variable for ease of use. Our notebooks expect to find it stored as `IONQ_API_KEY`.
4. An installation of the library you're wanting to run. You can install all libraries using one of the following methods:

   **Option 1: Using uv (Fastest - Recommended)**

   [uv](https://github.com/astral-sh/uv) is an extremely fast Python package installer and resolver:

   ```shell
   # Install uv (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install all dependencies
   uv pip install -e .
   ```

   **Option 2: Using Conda**

   ```shell
   conda env create -f environment.yml
   ```

   **Option 3: Using pip**

   ```shell
   pip install -e .
   ```

---

## Docker

For a reproducible environment with all dependencies pre-installed:

```shell
# Build the image (linux/x86_64 required for cudaq)
docker build --platform=linux/x86_64 -t ionq-notebooks .

# Run with your API key
docker run -p 8888:8888 -e IONQ_API_KEY="your_api_key_here" ionq-notebooks
```

Then open your browser to [http://localhost:8888](http://localhost:8888)

To persist notebook changes, mount the workspace as a volume:

```shell
docker run -p 8888:8888 -e IONQ_API_KEY="your_api_key_here" -v $(pwd):/workspace ionq-notebooks
```

---

## Usage

The samples are in the form of Jupyter notebooks, and you can view and run them using a local [Jupyter](http://jupyter.org/) installation, [VS Code](https://code.visualstudio.com/) (using the built-in Jupyter plugin), or [Google Colab](https://colab.research.google.com).

If you're unfamiliar with Jupyter but you're used to a traditional IDE or code editor, VS Code is probably the right choice for you.

#### Jupyter Notebooks

1. From your terminal, navigate to this repository and run the following command from within this directory:

   ```shell
   jupyter notebook
   ```

1. Once the server is started, it should automatically open your browser. In case it doesn't, you can navigate directly to it by pointing your browser at [http://localhost:8888](http://localhost:8888)
1. Navigate to the location of a `.ipynb` file and open it. If you don't have a particular SDK in mind, we recommend starting with `qiskit`, as its the most commonly used library today.

#### VS Code

1. Open the folder in VS Code and navigate to a `.ipynb` file and open it.
1. If it's your first time using it, it will suggest a number of plugins that you may need to install before the notebook will be fully functional.
1. At the top-right of the screen, click on `Select Kernel` and choose an appropriate Python runtime to run the notebook in.

#### Cloud

1. Open the notebook by clicking on the ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg) badge located in each notebook. Or open this repository in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ionq-samples/getting-started/HEAD)

---

## Support

For support, you can submit issues or PRs in this repository. Alternatively, you can contact us at [support@ionq.com](mailto:support@ionq.com?subject=SDK%20help).
