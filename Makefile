ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: run_tests

update: fetch_upstream fetch_patches

tests:
	$(MAKE) -C ./tests

fetch_upstream:
	./fetch_upstream.py

fetch_patches:
	./fetch_patches.py

.PHONY: livecd
livecd:
	$(MAKE) -C ./livecd
