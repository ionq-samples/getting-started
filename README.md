# IonQ Quantum Computing Samples

Welcome to the IonQ Quantum Computing Samples repository! This repository is your guide to exploring quantum computing using the IonQ platform with different quantum programming frameworks. These samples will introduce you to writing, manipulating, and executing quantum circuits with IonQ quantum computers.

## What's Inside?

This repository contains a range of examples demonstrating the use of various quantum computing frameworks on IonQ's platform. Each sub-directory holds an illustrative example for a specific framework, each set up to run a Bell State preparation circuit. The frameworks currently included are:

1. **Cirq**
2. **CUDA Quantum**
3. **PennyLane**
4. **ProjectQ**
5. **Qiskit**

Each example includes a `main.ipynb` Jupyter notebook file that demonstrates the use of the respective framework to create and execute a quantum circuit. 

## Prerequisites

To use these samples, you will need:

- Python installed on your machine. 
- An API key from IonQ. This can be obtained from <https://cloud.ionq.com/settings/keys>.
- The Python libraries mentioned in the `requirements.txt` file.

To install the required Python libraries, navigate to the main directory of this repository and run the following command:

```shell
pip install -r requirements.txt
```

Remember to set your IonQ API key as an environment variable:

```shell
export IONQ_API_KEY=your_api_key_here
```

## How To Use

Each sample has its own `README.md` file explaining how to use it. However, the general steps are as follows:

1. Navigate to the specific framework's directory.
2. Open the `main.ipynb` Jupyter notebook.
3. Run the cells in the notebook. This will install the necessary packages, set up a connection to the IonQ service using your API key, create a quantum circuit, and execute the circuit.

You can run Jupyter notebook by typing the following command in your terminal:

```shell
jupyter notebook
```

Then, navigate to the corresponding notebook file (`.ipynb`) in your browser and execute the cells.

You can also run the notebooks directly in your browser using Google Colab. Each `README.md` in the subdirectories has an "Open in Colab" badge. Clicking on it will open the notebook in Google Colab.

## Contact Us

If you have any questions, issues, or other feedback about these samples, feel free to submit an issue or pull request on this repository, or reach out to us directly at [support@ionq.com](mailto:support@ionq.com?subject=SDK%20help).
