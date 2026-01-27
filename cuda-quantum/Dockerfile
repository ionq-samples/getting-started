# Start from a minimal Python 3.11 image
FROM --platform=linux/x86_64 python:3.11

# Install Jupyter and CUDA-Q
RUN pip install --no-cache-dir jupyter cudaq

# Copy the main CUDA-Q notebook and helper script into the container
COPY main.ipynb helpers.py /workspace/

# Set the working directory
WORKDIR /workspace

# Run Jupyter Notebook, listening on all interfaces with no auth token.
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=", "--allow-root"]
