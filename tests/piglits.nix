{ lib ? import ../nixpkgs/lib, pkgs ? import ../nixpkgs {} }:

let 

  customPiglit = args @ { ... }: import ./customPiglit.nix ({
    pkgs = pkgs;
    lib = lib;
  } // args);

  mesa_arb_shader_subroutine = pkgs.fetchgit {
    url = "git://people.freedesktop.org/~airlied/mesa";
    rev = "1c57fff7136eecc33554e600913a8a1f6c96ecc1";
    sha256 = "5a1a760d217e2aff1549896a65a0a84cd06fa37ec092d989b23284396882c51c";
  };

  mesa_r600g-tess = pkgs.fetchgit {
    url = "git://people.freedesktop.org/~airlied/mesa";
    rev = "c045fe0224fecf04f6e27445243fc9787d41dd9c";
    sha256 = "32458e47f40b43e40bee521dc83543d523ed9dfa57aa035477e0cdd9bacacc6d";
  };

  mesa_nir-cse-hash-v2 = pkgs.fetchgit {
    url = "git://people.freedesktop.org/~cwabbott0/mesa";
    rev = "f9be7219ea246e338d121f874736d26a9a78ca5e";
    sha256 = "f5d885e292f36b0c524fd8b0355a1e0d765481bb6e23e51c6bca2558ee4f1027";
  };

  mesa_git = pkgs.fetchgit {
    url = "git://anongit.freedesktop.org/mesa/mesa";
    rev = "bd198b9f0a292a9ff4ffffec3a29bad23d62caba";
    sha256 = "c9a4202b347aeeda77ea413798564ef871127c58702192ae5311065c92148e60";
  };
in
rec {
  piglits.mesa_git = customPiglit { };
  piglits.mesa_arb_shader_subroutine = customPiglit { mesa_src = mesa_arb_shader_subroutine; };
  piglits.mesa_r600g-tess = customPiglit { mesa_src = mesa_r600g-tess; };
  piglits.mesa_nir-cse-hash-v2 = customPiglit { mesa_src = mesa_nir-cse-hash-v2; };
}
