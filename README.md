Simple angr Example
-------------------

This is a very simple example of how to use [angr](http://angr.io/).

Binary included is built using the Docker image provided for angr - [http://docs.angr.io/INSTALL.html#docker-install](http://docs.angr.io/INSTALL.html#docker-install)

A Docker image is also included for quick setup and execution of the example.

---------------------------
### Dockerfile Usage:
- Install & Start Docker
- Run `./scripts/startImage.sh` and cd into simple
- Run `./solve-simple.py`

### Manual Usage:

- Install Angr: [http://docs.angr.io/INSTALL.html](http://docs.angr.io/INSTALL.html)
- Run `./solve-simple.py` which should return `'a'` as the solution to the simple binary.

---------------------------
