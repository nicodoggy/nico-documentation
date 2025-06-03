# installing `guake` from source

[online documentation](https://guake.readthedocs.io/en/latest/user/installing.html#install-from-source)

<hr />

> Note: I highly recommend following the instructions in [_enabling-extra-packages.md](_enabling-extra-packages.md) as they make getting dependencies easier.

<hr />

1. Clone the repository at [https://github.com/Guake/guake.git](https://github.com/Guake/guake.git).

```bash
git clone https://github.com/Guake/guake.git
```

2. `cd` into the directory that you cloned the repository into.

3. To install dependencies, try to run this command:

```bash
./scripts/bootstrap-dev-fedora.sh run make
```

> There is also a `debian` and an `arch` shellscript file that you can use as opposed to `fedora`.

4. Run `make`:

```bash
make
sudo make install
```

## Dependencies
For your convenience, here's a list of the dependencies for Fedora as of May 30, 2025, according to `scripts/bootstrap-dev-fedora.sh`.

### Packages needed for execution
- `python3-devel`
- `python3-cairo`
- `python3-dbus`
- `python3-pip`
- `keybinder3`*
- `libwnck`*

```bash
sudo yum install python3-devel python3-cairo python3-dbus python3-pip keybinder3 libwnck 
```

###  Packages needed for making guake
- `gettext`
- `gsettings-desktop-schemas`
- `make`
- `pandoc`

```bash
sudo yum install gettext gsettings-desktop-schemas make pandoc 
```

### Packages needed for development
- `dconf-editor`
- `glade`*
- `poedit`*
- `gnome-tweak-tool`

```bash
sudo yum install dconf-editor glade poedit gnome-tweak-tool
```

### Optional packages for execution
- `libutempter`
- `numix-gtk-theme`*


```bash
sudo yum install libutempter numix-gtk-theme 
```

> \* Not found on RHEL 10.0 (see section below)

### The following dependencies were not found on RHEL 10.0:
- `keybinder3`
- `libwnck`
- `glade`
- `poedit`
- `numix-gtk-theme`**

> ** Not required by `guake`.
 
 <hr />

> If keybinder3 is not found on your package manager, you will need to [install `keybinder-3.0` from source](keybinder.md) if you do not have it already.

Then, try to run guake by typing "guake" into a terminal and pressing enter.

If you get this message
```
[ERROR] missing mandatory dependency: Keybinder 3
[ERROR] missing at least one system dependencies. You need to install additional packages for Guake to run
[ERROR] On Debian/Ubuntu you need to install the following libraries:
    sudo apt-get install -y --no-install-recommends \
        gir1.2-keybinder-3.0 \
        gir1.2-notify-0.7 \
        gir1.2-vte-2.91 \
        gir1.2-wnck-3.0 \
        libkeybinder-3.0-0 \
        libutempter0 \
        python3 \
        python3-dbus \
        python3-gi \
        python3-pip
```

1. Make sure you installed keybinder from source.

<hr />

See the [online documentation](https://guake.readthedocs.io/en/latest/user/installing.html#install-from-source) for further instructions.


