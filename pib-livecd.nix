# This module defines a NixOS installation CD that contains X11 and
# KDE 4.

{ config, lib, pkgs, ... }:

with lib;

# XXX: These are specific piglits that are being built (for no good
# reason other than to make sure they build?)
#with import @srcdir@/../tests/piglits.nix { inherit lib; inherit pkgs; };

let
# XXX: The tarball, which used to be built by autotools as its dist
# tarball, will be replaced by a nix derivation (which may use
# autotools internally, although I probably won't bother) that gathers
# the latest git checkout from mesa.
#  tarball_name = "@PACKAGE_NAME@-@PACKAGE_VERSION@";
in
{
  /* XXX: I'm not sure if this import will actually work... */
  /* XXX: Don't use an absolute path here for the import */
  imports = [ "/home/auntieneo/code/piab/nixpkgs/nixos/modules/installer/cd-dvd/installation-cd-base.nix" ];

  # Provide wicd for easy wireless configuration.
  #networking.wicd.enable = true;

  environment.systemPackages =
    [
      pkgs.git
      pkgs.gnumake

      # Include some piglit tests
#      piglits.mesa_nir-cse-hash-v2  # XXX
    ];

  # Provide networkmanager for easy wireless configuration.
#  networking.networkmanager.enable = true;
#  networking.wireless.enable = mkForce false;

  services.xserver = {
    enable = true;

    # Start X by default
    autorun = true;

    # Auto-login as root.
    displayManager.auto.enable = true;
    displayManager.auto.user = "root";
    displayManager.sessionCommands =
    let
      start_piab = builtins.toFile "start_piab.sh" ''
        #!/usr/bin/env sh
        # We probably just booted, so we need to wait a bit for the network
        echo "Waiting for the network..."
        sleep 10 &&
        mkdir repos &&
#        echo "Extracting mesa repository..." &&
#        tar xzf /iso/mesa.tar.gz -C repos/ &&
#        echo "Extracting piglit repository..." &&
#        tar xzf /iso/piglit.tar.gz -C repos/ &&
        ./pib-tui/pib-tui.py
#        mkdir piab-build && cd piab-build &&
#        ../piab/configure && /usr/bin/env make tests
      '';
    in
    ''
        ${pkgs.xterm}/bin/xterm \
            -fn 10x20 -bg black -fg LightGray \
            -hold -e 'sh ${start_piab}' &
        waitPID=$!
    '';

    desktopManager.default = mkForce "none";

    windowManager = {
      # We just want to fill the screen with a terminal; no nonsense.
      # Honestly I don't even know how to use ratpoison.
      ratpoison.enable = true;
      default = "ratpoison";
    };
  };

  system.activationScripts.includePIB = let
    pib-tui = pkgs.callPackage ./pib-tui.nix { };
  in stringAfter [ "users" ]
  ''
    # XXX: This symlink provides access to the pib nix code such that
    # the PIB TUI can later build its own piglits.
    ln -s ${pib-tui} /root/pib-tui
  '';

  system.activationScripts.xtermColors = let
    xdefaults = builtins.toFile "Xdefaults" ''
      # tango color scheme (because the default xterm colors are ugly)
      xterm*color0: #1e1e1e
      xterm*color1: #cc0000
      xterm*color2: #4e9a06
      xterm*color3: #c4a000
      xterm*color4: #3465a4
      xterm*color5: #75507b
      xterm*color6: #0b939b
      xterm*color7: #d3d7cf
      xterm*color8: #555753
      xterm*color9: #ef2929
      xterm*color10: #8ae234
      xterm*color11: #fce94f
      xterm*color12: #729fcf
      xterm*color13: #ad7fa8
      xterm*color14: #00f5e9
      xterm*color15: #eeeeec
    '';
  in stringAfter [ "users" ]
  ''
    ln -s ${xdefaults} /root/.Xdefaults
  '';

  # Add some git repositories to the livecd to reduce the burden on
  # the servers
  # FIXME: These tarballs use up a lot of space in livecd RAM after
  # being extracted. It would be much better to add these repositories
  # un-archived to the iso, but the interface isoImage.contents
  # provides makes this difficult.
  isoImage.contents =
    [
    /*
      { source = "@abs_builddir@/repos/mesa.tar.gz";
        target = "/mesa.tar.gz";
      }
      { source = "@abs_builddir@/repos/piglit.tar.gz";
        target = "/piglit.tar.gz";
      }
      */
    ];

#  system.activationScripts.installerDesktop = let
#    openManual = pkgs.writeScript "nixos-manual.sh" ''
#      #!${pkgs.stdenv.shell}
#      cd ${config.system.build.manual.manual}/share/doc/nixos/
#      konqueror ./index.html
#    '';
#
#    desktopFile = pkgs.writeText "nixos-manual.desktop" ''
#      [Desktop Entry]
#      Version=1.0
#      Type=Application
#      Name=NixOS Manual
#      Exec=${openManual}
#      Icon=konqueror
#    '';
#
#  in ''
#    mkdir -p /root/Desktop
#    ln -sfT ${desktopFile} /root/Desktop/nixos-manual.desktop
#    ln -sfT ${pkgs.kde4.konsole}/share/applications/kde4/konsole.desktop /root/Desktop/konsole.desktop
#    ln -sfT ${pkgs.gparted}/share/applications/gparted.desktop /root/Desktop/gparted.desktop
#  '';
}
