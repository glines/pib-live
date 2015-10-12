all: run_tests

update: fetch_upstream fetch_patches

run_tests:

fetch_upstream:
	./fetch_upstream.py

fetch_patches:
	./fetch_patches.py

#livecd:
#	nix-build -A iso_piab.x86_64-linux -o livecd ./nixpkgs/nixos/release.nix

livecd:
	nix-build -E '(import ./nixpkgs/nixos/release.nix {}).makeIso { module = ./piab-livecd.nix; type = "graphical"; system = "x86_64-linux"; }' -o livecd
