SCRIPT_DIR=$(realpath $(shell dirname $(lastword $(MAKEFILE_LIST))))
PROJECT_ROOT=$(realpath $(shell dirname $(lastword $(MAKEFILE_LIST)))/../)
TAG ?= latest
GOOGLE_PROJECT_ID := bd17-gcp

VIRTUALENV = $(shell which virtualenv)

VENVS= ${HOME}/envs
PYTHON_VER = $(shell which python3.7)
VENV= ${VENVS}/medulla-charon

default: menu

venv:
	$(VIRTUALENV) -p ${PYTHON_VER} ${VENV}

uninstall:
	rm -fr *.egg-info
	rm -fr ${VENV}

install: setup uninstall venv update

setup:
	sudo mkdir -p /var/log/datalake; sudo chmod 777 /var/log/datalake

update:
	. ${VENV}/bin/activate; pip install -U .

develop:
	. ${VENV}/bin/activate; pip install -Ue .
	. ${VENV}/bin/activate; pip install -r requirements-dev.txt


menu:
	@echo '# datamgr (Makefile)'
	@echo
	@echo 'install - install the package'
	@echo 'update -  update the package'
	@echo 'uninstall - remove installation'
	@echo
