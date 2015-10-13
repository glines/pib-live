# This module defines a NixOS installation CD that contains X11 and
# KDE 4.

{ config, lib, pkgs, ... }:

with lib;

with import ../tests/piglits.nix { inherit lib; inherit pkgs; };

{
  imports = [ ../nixpkgs/nixos/modules/installer/cd-dvd/installation-cd-base.nix ];

  # Provide wicd for easy wireless configuration.
  #networking.wicd.enable = true;

  environment.systemPackages =
    [
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
    displayManager.sessionCommands = ''
        # We probably just booted, so we need to wait a bit for the network
        ${pkgs.xterm}/bin/xterm -bg black -fg white -hold -e 'sleep 10 && cd /root/piab && ${pkgs.gnumake}/bin/make tests' &
        waitPID=$!
    '';

    desktopManager.default = mkForce "none";

    windowManager = {
      # We just want to fill the screen with a terminal; no nonsense.
      # Honestly I don't even know how to use ratpoison.
      ratpoison.enable = true;
      default = "ratpoison";
    };

#    displayManager.session = singleton
#      { name = "xterm-piab";
#        manage = "desktop";
#        start = ''
#          ${pkgs.xterm}/bin/xterm -hold -e 'cd /root/piab && ${pkgs.gnumake}/bin/make tests' &
#          waitPID=$!
#        '';
#      };
  };


  system.activationScripts.includePIAB = let
    piab = pkgs.callPackage ./piab.nix { };
  in ''
    ln -s ${piab} /root/piab
  '';

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
