# Cuda Quantum

First run the Dockerfile:

```shell
docker build -t cuda-quantum -f Dockerfile . && docker run -p 8888:8888 -it cuda-quantum
```

Then start the Jupyter server:

```shell
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```
