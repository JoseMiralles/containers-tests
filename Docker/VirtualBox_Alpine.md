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

# Configure VM for host access

**THIS CURRENTLY KILLS INTERNET ACCESS, DISABLE SECOND ADAPTER FOR NOW**

1. On VirtualBox, open `File`, `Host Network Manager`, and click on the add button to add a new network.
1. Then open the settings for the Alpine VM, `Network`, `Adapter 2`, check, `Enable Network Adapter`, set `Attached to: Host-only adapter`, set `Name: vboxnet0`.

# Setup Alpine Linux

1. Start the VM.
1. Login as `root`
1. Setup Alpine:
    - To install to disk: https://wiki.alpinelinux.org/wiki/Install_to_disk
    - To run from CD `setup-alpine -q`, enter `us` for keyboard layout and keyboard option.
1. Test the network with `ping google.com`.
    - Press `ctr z` to stop it after a few pings.
1. Run `ifconfig`, and write down the IP address somewhere.

<br>

# Installing Packages in Alpine Linux

- Install Vim: `apk add vim`
- Search for nano: `apk search cmd:nano`
    - Easier to use: https://pkgs.alpinelinux.org/packages
- Install multiple: `apk add vim nano`
- Uninstall: `apk del nano`
- Uninstall package + dependencies: `apk del -r nano`
- Preview uninstallation: `apk del -sr nano`

# Installing Python and PIP

1. Run `apk add python3`
2. Install Pip: https://pip.pypa.io/en/stable/installation/
    - Basically run: `python3 -m ensurepip --upgrade`
3. Install Pipenv: `python3 -m pip install --user pipenv`

To use pipenv: `python3 -m pipenv`