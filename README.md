# IonQ Quantum Computing Samples

Python samples demonstrating quantum computing on IonQ's platform using popular quantum libraries. A great starting point for exploring quantum computation.

For advanced examples implementing specific algorithms, check out the [ionq-samples](https://github.com/ionq-samples) organization.

---

## Quick Start

### Prerequisites

- Python 3.10-3.13
- [IonQ API key](https://cloud.ionq.com/settings/keys) (set as `IONQ_API_KEY` environment variable)

### Installation

**Using pip:**
```bash
pip install -e .
```

**Using uv (faster):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install -e .
```

**Using conda:**
```bash
conda env create -f environment.yml
```

### Running Notebooks

**Jupyter:**
```bash
jupyter notebook
```

**VS Code:**
Open any `.ipynb` file and select a Python kernel.

**Cloud:**
Click the ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg) badge in each notebook.

---

## Docker

Run in a containerized environment:

```bash
# Build
docker build --platform=linux/x86_64 -t ionq-notebooks .

# Run
docker run -p 8888:8888 -e IONQ_API_KEY="your_api_key" ionq-notebooks
```

Open [http://localhost:8888](http://localhost:8888) in your browser.

---

## Development

### Running Tests

```bash
# All tests
pytest tests/

# Parallel execution
pytest -n auto tests/

# Specific notebook
pytest tests/test_notebooks.py::test_notebook_execution[qiskit.ipynb]

# With custom timeout
NBEXEC_TIMEOUT_SECONDS=900 pytest tests/
```

GitHub Actions automatically tests all notebooks on every push.

---

## Support

Submit issues or PRs in this repository, or contact [support@ionq.com](mailto:support@ionq.com?subject=SDK%20help).
