AC_INIT([piab], [0.0.1])
AC_CONFIG_FILES([Makefile livecd/Makefile livecd/piab-livecd.nix livecd/repos/Makefile tests/Makefile])

AC_ARG_WITH([nixpkgs],
    AS_HELP_STRING([--with-nixpkgs=DIR], [full path to the Nix Packages tree]))
# FIXME: Support relative paths here
AC_SUBST([nixpkgs], ["$with_nixpkgs"])

AC_OUTPUT
