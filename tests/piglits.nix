{ lib ? import ../nixpkgs/lib, pkgs ? import ../nixpkgs {} }:

let 

  customPiglit = args @ { ... }: import ./customPiglit.nix ({
    pkgs = pkgs;
    lib = lib;
  } // args);

  mesa_arb_shader_subroutine = pkgs.fetchgit {
    url = "file:///home/auntieneo/code/mesa";
    rev = "refs/remotes/airlied/arb_shader_subroutine";
    sha256 = "5a1a760d217e2aff1549896a65a0a84cd06fa37ec092d989b23284396882c51c";
  };

  mesa_r600g-tess = pkgs.fetchgit {
    url = "file:///home/auntieneo/code/mesa";
    rev = "refs/remotes/airlied/r600g-tess";
    sha256 = "32458e47f40b43e40bee521dc83543d523ed9dfa57aa035477e0cdd9bacacc6d";
  };

  mesa_nir-cse-hash-v2 = pkgs.fetchgit {
    url = "file:///home/auntieneo/code/mesa";
    rev = "refs/remotes/cwabbott0/nir-cse-hash-v2";
    sha256 = "f5d885e292f36b0c524fd8b0355a1e0d765481bb6e23e51c6bca2558ee4f1027";
  };

  mesa_git = pkgs.fetchgit {
    url = "file:///home/auntieneo/code/mesa";
    rev = "refs/heads/master";
    sha256 = "0baa3c0b0f090d71ad1410e832c3316e3ffebffd94af39f11b5dc891e77b8a17";
  };
in
rec {
  piglits.mesa_git = customPiglit { };
  piglits.mesa_arb_shader_subroutine = customPiglit { mesa_src = mesa_arb_shader_subroutine; };
  piglits.mesa_r600g-tess = customPiglit { mesa_src = mesa_r600g-tess; };
  piglits.mesa_nir-cse-hash-v2 = customPiglit { mesa_src = mesa_nir-cse-hash-v2; };
}
