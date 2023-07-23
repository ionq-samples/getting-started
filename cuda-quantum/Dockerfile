# We start from a minimal Python 3.11 image
FROM --platform=x86_64 python:3.11

# Install Jupyter
RUN pip install jupyter cuda-quantum

# Copy the main.ipynb file into the container
COPY main.ipynb /workspace/

# Set the working directory
WORKDIR /workspace

# The command to run when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--allow-root"]
