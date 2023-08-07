# IonQ Quantum Computing Samples

This repository contains Python samples exploring quantum computing on IonQ's platform using various quantum programming libraries.

## Setup

To set up, follow the instructions below:

1. Download and install [Python](https://www.python.org/downloads/).

2. Obtain an [IonQ API key](https://cloud.ionq.com/settings/keys).

    Use `export` to set the IonQ API key as an environment variable:

    ```shell
    export IONQ_API_KEY=api_key_here # Windows: set IONQ_API_KEY=api_key_here
    ```

3. Install the required [Python libraries](requirements.txt).

    Run `pip` in your terminal to install the required libraries:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

The samples are in the form of Jupyter notebooks, and you can run them using either Google Colab or your local Jupyter installation.

- For Google Colab, open the notebook by clicking on the ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg) badge located in each subdirectory's `README.md`.

- For Jupyter notebooks, use the following command to start a local Jupyter server:

    ```shell
    jupyter notebook
    ```

    Then, navigate to the location of a `.ipynb` file and open it.

## Support

For support, you can submit issues or PRs in this repository. Alternatively, you can contact us at [support@ionq.com](mailto:support@ionq.com?subject=SDK%20help).
