# README

## Introduction

This is a simple demonstration for how to build a docker image iteratively, changing the contents of the image at each turn.
The script will run 10 iterations and create images `iterate-demo:iter-N` for N = 0 to 9. Running the image produces a different output each time.

## Dependencies

- a working local installlation of `docker`
- tested with Anaconda Python 3.8
- Docker SDK for python installed (see [docs](https://docker-py.readthedocs.io/en/stable/index.html)]

## Running the example

```
python iterate-build.py
```

## Cleaning up images

Clean up images and intermediate images we just created:
```sh
docker container prune -f
docker rmi $(docker images -q iterate-demo:*)
docker rmi $(docker images -f dangling=true -q)
```
