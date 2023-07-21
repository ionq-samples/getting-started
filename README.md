# IonQ Quantum Framework Examples

This repository contains examples of using different quantum frameworks with IonQ quantum computers. IonQ is a pioneer in the world of trapped ion quantum computing and these examples aim to help you get started with using the different quantum frameworks on IonQ computers.

We provide examples using several popular quantum computing frameworks:
- [Qiskit](https://qiskit.org/)
- [Cirq](https://quantumai.google/cirq)
- [CUDA Quantum](https://developer.nvidia.com/cuda-quantum)
- [ProjectQ](https://projectq.ch/)
- [PennyLane](https://pennylane.ai/)

Each directory contains a README and a Jupyter notebook (`main.ipynb`) detailing how to implement and run a simple quantum circuit using that specific framework. Additionally, a `requirements.txt` file is present in the root directory containing the necessary dependencies for these examples.

## Setup

Python 3.11 or later is required to run the examples in this repository. To install all necessary dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## How to use

You can choose to run these examples in Google Colab or locally on your machine.

To run in Google Colab, navigate to the specific framework directory and click on the ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) badge.

To run the examples locally, follow these steps:

1. Clone this repository: `git clone https://github.com/ionq-samples/getting-started.git`
2. Navigate to the directory of the framework you wish to explore: `cd getting-started/<framework>`
3. Open the Jupyter notebook: `jupyter notebook main.ipynb`

Additional instructions and comments can be found in the README file within each framework directory.

## Contribution and Support

All contributions are welcome! Feel free to propose changes, report bugs, or suggest improvements by creating issues or providing pull requests.

If you need assistance or encounter any problems, you can:

- Create an [issue](https://github.com/ionq-samples/getting-started/issues/new) and tag @splch or @mocha
- Or email [support](mailto:support@ionq.com?subject=SDK%20help)

We appreciate your interest in this project and look forward to your contributions and questions.
