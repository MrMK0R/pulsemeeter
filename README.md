# Pulsemeeter
A frontend to ease the use of pulseaudio's routing capabilities, mimicking voicemeeter's workflow

[![pypi](https://img.shields.io/badge/pypi-v1.2.13-blue)](https://pypi.org/project/pulsemeeter/)
[![AUR](https://img.shields.io/badge/AUR-V1.2.12-cyan)](https://aur.archlinux.org/packages/pulsemeeter/)
[![AUR](https://img.shields.io/badge/AUR-pulsemeeter--git-red)](https://aur.archlinux.org/packages/pulsemeeter-git/)
[![Discord](https://img.shields.io/badge/chat-Discord-lightgrey)](https://discord.gg/ekWt9NuEWv)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Donate](https://img.shields.io/badge/donate-PayPal-green.svg)](https://www.paypal.com/donate/?hosted_button_id=6DSVJ3V3RCVT8)
[![Donate](https://img.shields.io/badge/donate-Patreon-yellow.svg)](https://www.patreon.com/theRealCarneiro)

### Wiki: \[[Installation](https://github.com/theRealCarneiro/pulsemeeter/wiki/Installation)\] \[[How to use](https://github.com/theRealCarneiro/pulsemeeter/wiki/Installation)\]

![](https://i.imgur.com/L4KZEqV.png)
(This screenshot was taken while using ant dracula gtk theme, it will use your theme)

# Table of Contents
- **[Features](#features)**
- **[Installation](#installation)**
    - [Dependencies](#dependencies)
    - [Arch](#arch-aur)
    - [Pypi install](#any-distro)
    - [Manual/Git install](#build-from-source)
- **[Auto Start](#start-devices-on-startup)**
- **[Discord Server](#discord-server)**

# Features
 - Create virtual inputs and outputs
 - Route audio from one device to another
 - Volume control
 - Equalizer for hardware and virtual outputs
 - Rnnoise noise reduction (same algorithm as [noisetorch](https://github.com/lawl/NoiseTorch)) for hardware inputs

# Installation

## Installation Dependencies

Before you start using PulseMeeter, make sure you have the following dependencies installed on your system. Visit the dependencies section in the wiki for in-depth information tailored to your specific system.
Required Dependencies:

- pip
- python3
- libappindicator3
- gobject-introspection-1.0
- libpulse
- libappindicator3-tools
- libdbusmenu-gtk3-dev
- libdbusmenu-gtk4
- libdbusmenu-glib-dev

# Installation Commands:

### For Ubuntu/Debian:
```sh
sudo apt-get update && sudo apt install python3 python3-pip libappindicator3-1 gobject-introspection libpulse0 libdbusmenu-gtk3-dev libdbusmenu-glib-dev

```
### For Fedora:
```sh
sudo pacman -Syu && sudo pacman -S python python-pip libappindicator-gtk3 gobject-introspection-runtime pulseaudio libdbusmenu-gtk3 libdbusmenu-glib
```
### For Arch Linux:

```sh 
sudo dnf update && sudo dnf install python3 python3-pip libappindicator gobject-introspection pulseaudio-libs libdbusmenu-gtk3 libdbusmenu-glib
```


### Python Dependencies
Pip will automaticly install these dependencies
 - [pygobject](https://pypi.org/project/PyGObject)
 - [pulsectl](https://pypi.org/project/pulsectl)
 - [setuptools](https://pypi.org/project/setuptools/)


### Optional Dependencies
These dependencies are optional and will enable new features in the application
- [noise-suppression-for-voice](https://github.com/werman/noise-suppression-for-voice) for noise reduction
- [swh-plugins](https://github.com/swh/ladspa) for equalizers (apt/dnf/pacman packages available)
- [pulse-vumeter](https://github.com/theRealCarneiro/pulse-vumeter) for volume level information

## Any distro

### Single user
When installing for a single user (without sudo) you need to add ~/.local/bin to your path, [this section](#add-local-bin-to-path) will show you how to do it
```sh

pip3 install pulsemeeter
```
### For all users
```sh
sudo pip3 install pulsemeeter
```

## Arch (AUR)
Two packages are available in the AUR: [pulsemeeter](https://aur.archlinux.org/packages/pulsemeeter) and [pulsemeeter-git](https://aur.archlinux.org/packages/pulsemeeter-git/).

## Build from source:

### Single user
When installing for a single user (without sudo) you need to add ~/.local/bin to your path, [this section](#add-local-bin-to-path) will show you how to do it
```sh
git clone https://github.com/theRealCarneiro/pulsemeeter.git
cd pulsemeeter
python3 -m venv myenv
source myenv/bin/activate
pip3 install .
```

### For all users
```sh
git clone https://github.com/theRealCarneiro/pulsemeeter.git
cd pulsemeeter
python3 -m venv myenv
source myenv/bin/activate
sudo pip3 install .
```

### For Dev
```sh
git clone https://github.com/theRealCarneiro/pulsemeeter.git
cd pulsemeeter
python3 -m venv myenv
source myenv/bin/activate
pip3 install -e .

```

### Uninstall

```sh
pip3 uninstall pulsemeeter
sudo pip3 uninstall pulsemeeter
```

### Add local bin to PATH

When installing for a single user, you to need to have $HOME/.local/bin in your PATH, to do this, you'll have to add this line to your ~/.profile (or .zprofile if you use zsh as your login shell) file
```sh
export PATH="$HOME/.local/bin:$PATH"
```

## Common Errors
When starting pulsemeeter and the error "virual_input_b3" could not be started. To solve the issue, kill all pulsemeeter instances, and kill all pulseaudio instances and restart them up. The command should look similar to:

ENSURE PULSEMEETER IS CLOSED, THE ERROR WILL POP UP IF IT IS NOT CLOSED.
```sh
pkill pulsemeeter && rm -rf ~/.config/pulsemeeter/ && pulseaudio -k && pulseaudio --start
&& pkill pulsemeeter && pulseaudio -k && pulseaudio --start
```

Settings Not Saving?
Ensure pulsemeeter is closed, navigate to `~/.config/pulsemeeter`, and delete the config.json

## Start devices on startup
All connections and devices will be restored with the command `pulsemeeter init`

## Discord Server
If you want to get updates about new features, patches or leave some sugestions, join our [discord server](https://discord.gg/ekWt9NuEWv)

## Special thanks to

* [xiph.org](https://xiph.org)/[Mozilla's](https://mozilla.org) excellent [RNNoise](https://jmvalin.ca/demo/rnnoise/).
* [@werman](https://github.com/werman/)'s [noise-suppression-for-voice](https://github.com/werman/noise-suppression-for-voice/)
* [@swh](https://github.com/swh)'s [swh-plugins](https://github.com/swh/ladspa)
