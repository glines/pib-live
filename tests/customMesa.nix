{
  lib, pkgs,
	mesa_src ? false,
  debug ? false
}:

let
	# Set a default Mesa source if one is not specified.
	_mesa_src = if mesa_src != false then mesa_src else
		(pkgs.callPackage ../nixpkgs/pkgs/development/libraries/mesa/default.nix { grsecEnabled = false; }).src;

	# We need a newer version of libdrm than nixpkgs provides.
	libdrm_2_4_65 = pkgs: (pkgs.libdrm.overrideDerivation (attrs: rec {
		name = "libdrm-${version}";
		version = "2.4.65";

		src = pkgs.fetchurl {
			url = "http://dri.freedesktop.org/libdrm/${name}.tar.bz2";
			sha256 = "1i4n7mz49l0j4kr0dg9n1j3hlc786ncqgj0v5fci1mz7pp40m5ki";
		};
	}));
in
lib.makeOverridable (args: lib.overrideDerivation pkgs.mesa_noglu (attrs: rec {
			name = "mesa-noglu-${version}";
			version = "git";

			enableParallelBuilding = true;
			src = _mesa_src;
			nativeBuildInputs = [ pkgs.pythonPackages.Mako ] ++ attrs.nativeBuildInputs;
		}));
