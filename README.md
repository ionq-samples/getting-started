# IonQ Quantum Computing Samples

This repository contains Python samples exploring quantum computing on IonQ's platform using various quantum programming libraries. 

- [Cirq](./cirq)
- [CUDA Quantum](./cuda-quantum)
- [PennyLane](./pennylane)
- [ProjectQ](./projectq)
- [Qiskit](./qiskit)

## Setup

To set up, follow the instructions below:

1. Make sure Python is installed on your machine.
2. Obtain an IonQ API key [here](https://cloud.ionq.com/settings/keys).
3. Install the necessary Python libraries from `requirements.txt`.

To install the libraries, run the following command in your terminal:

```shell
pip install -r requirements.txt
```

To set the IonQ API key as an environment variable, use the following command:

```shell
export IONQ_API_KEY=your_api_key_here
```

## Running Notebooks

The samples are in the form of Jupyter notebooks, and you can run them using either Google Colab or your local Jupyter notebook installation.

- For Google Colab, open the notebook by clicking on the ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg) badge located in each subdirectory's `README.md`.

- For Jupyter notebooks, use the following command to start a local Jupyter server:

```shell
jupyter notebook
```

Then, navigate to the location of a `.ipynb` file and open it.

## Support

For support, you can submit issues or PRs in this repository. Alternatively, you can contact us at [support@ionq.com](mailto:support@ionq.com?subject=SDK%20help).
