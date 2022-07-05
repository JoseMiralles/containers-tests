# installing and creating machine

1. Install Virtual Box and the extension pack.
1. Create a new VM:
    - Name it `alpine`
    - Set type to `Linux`
    - Set version to `Other Linux (64-bit)`
    - Leave all the default settings.
1. Download the `Alpine Linux, Virtual, X86_64` iso from https://www.alpinelinux.org/downloads
1. In the Virtual Box manager, click on `[Optical Drive] Empty`, to the right of `IDE Secondary Device 0:`, and then click on `Choose/Create Disk Image`.
1. Click `Add`, and select the Alpine Linux iso.
1. Make sure that the iso is highlighted, and click on `choose`.

# Setup Alpine Linux

1. Start the VM.
1. Login as `root`
1. Run: `setup-alpine -q`
1. Enter `us` for the keyboard layout as well as for the keyboard option.
1. Test the network with `ping google.com`.
    - Press `ctr z` to stop it after a few pings.

<br>

# Installing Packages in Alpine Linux

- Install Vim: `apk add vim`
- Search for nano: `apk search cmd:nano`
    - Easier to use: https://pkgs.alpinelinux.org/packages
- Install multiple: `apk add vim nano`
- Uninstall: `apk del nano`
- Uninstall package + dependencies: `apk del -r nano`
- Preview uninstallation: `apk del -sr nano`