{ lib, stdenv, makeWrapper, python, pythonPackages, pkgs }:

stdenv.mkDerivation rec {
  name = "pib-tui-${version}";
  version = "XXX";

  /* FIXME: This should use fetchurl... maybe? */
  src = ./pib-tui;

  buildInputs = [ makeWrapper python ];
  propagatedBuildInputs = with pythonPackages; [ GitPython twisted urwid ];

  /* FIXME: Maybe these piglit tests should be in their own package? */
#  buildPhase =
#  with (import @piab_srcdir@/../tests/piglits.nix { inherit lib; inherit pkgs; });
#  ''
#    # We build a few select piglit tests, mostly for convenience. The livecd user
#    # will most likely build their own tests.
#    mkdir -p ./tests/piglits
#  '';
#    ln -s ${piglits.mesa_arb_shader_subroutine} ./tests/piglits/mesa_arb_shader_subroutine

  buildPhase = "";

  installPhase = ''
    mkdir "$out"
    cp -R ./* "$out"/

    wrapProgram "$out"/pib-tui.py \
      --prefix PYTHONPATH : "$PYTHONPATH"
  '';
}
