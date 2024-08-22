#!/usr/bin/make

SHELL=/bin/bash

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: setup
setup:  ## Setups environment
	virtualenv .
	./bin/pip install --upgrade pip
	./bin/pip install -r requirements.txt

.PHONY: pyinstaller
pyinstaller:  ## Builds the executable with pyinstaller
	./bin/pyinstaller -y imio-scan-helpers.spec
	if test -f configuration.json;then ln -s ../../configuration.json dist/imio-scan-helpers;fi

.PHONY: run
run:  ## Runs locally the main script with opt options (make run opt='-r main-99')
	./bin/python imio/scan_helpers/main.py ${opt}

.PHONY: tests
tests:  ## Runs tests
	# can be run by example with: make tests opt='-k "test_copy"'
	bin/python imio/scan_helpers/tests.py ${opt}

.PHONY: cleanall
cleanall:  ## Cleans all installed files
	rm -fr bin build dist include lib
