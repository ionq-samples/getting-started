# IonQ Quantum Computing Samples

Welcome to the IonQ Quantum Computing Samples repository! This repository provides examples of using different quantum programming frameworks with IonQ quantum computers.

The code samples are presented in the form of Jupyter notebooks, which are interactive documents that contain live code, equations, visualizations, and narrative text.

## Content

Here are the included samples:

- [Cirq](./cirq/README.md): A Python library for writing, manipulating, and optimizing quantum circuits at the level of individual quantum bits and quantum gates.

- [CUDA Quantum](./cuda-quantum/README.md): An example using Nvidia's CUDA Quantum.

- [PennyLane](./pennylane/README.md): A Python library for differentiable programming of quantum computers. Train a quantum computer the same way as a neural network!

- [ProjectQ](./projectq/README.md): An open-source software framework for quantum computing.

- [Qiskit](./qiskit/README.md): IBM's open-source quantum computing software development kit (SDK).

## Requirements

In order to run these samples, you'll need to install several Python libraries. You can do so by running:

```shell
pip install -r requirements.txt
```

Most importantly, you'll need an IonQ API key to run computations on IonQ quantum computers. You can obtain it from <https://cloud.ionq.com/settings/keys> and set it by running `export IONQ_API_KEY=your_api_key_here`.

## Usage

Each sample has its own `README.md` file explaining how to use it. In general, you can start Jupyter notebook by running:

```shell
jupyter notebook
```

Then, navigate to the corresponding notebook file (`.ipynb`) and run the cells.

## Contact

If you have any questions, feel free to open an issue or reach out to [support](mailto:support@ionq.com?subject=SDK%20help).
