ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: tests

.PHONY: tests
tests:
	$(MAKE) -C ./tests

.PHONY: livecd
livecd:
	$(MAKE) -C ./livecd
