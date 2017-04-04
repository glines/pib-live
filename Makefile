all: result

.PHONY: result
result:
	nix-build ./default.nix --show-trace

.PHONY: test
test: result
	qemu-kvm -cdrom ./result/iso/nixos-graphical-*.iso -m 1G
