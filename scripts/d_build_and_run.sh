docker build -t jupyter-nbs -f Dockerfile .

docker run --env PORT=8888 -it -p 8888:8888 jupyter-nbs
