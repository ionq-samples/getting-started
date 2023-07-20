# Use the Nvidia CUDA Quantum image built for the AMD64 platform as the base image
FROM --platform=linux/amd64 ghcr.io/nvidia/cuda-quantum:latest

# Update PATH environment variable
ENV PATH=$PATH:/home/cudaq/.local/bin/

# Install Jupyter
RUN pip3 install jupyter

# Add your main.ipynb file to the /workspace directory of the container.
# Make sure this Dockerfile and your main.ipynb file are in the same directory on your local machine
COPY main.ipynb /workspace/

# Make the workspace directory as the working directory
WORKDIR /workspace

# When the container is run, start the Jupyter notebook server
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]

# Expose the port the app runs in
EXPOSE 8888