#!/bin/bash

docker build -t angr-simple .
docker run -it angr-simple
