let
  makeIso = (import ./nixpkgs/nixos/release.nix {}).makeIso;
in
makeIso {
  module = ./pib-livecd.nix;
  type = "graphical";
  system = "x86_64-linux"; }
