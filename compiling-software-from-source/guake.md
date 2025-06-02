# installing `guake` from source
[online documentation](https://guake.readthedocs.io/en/latest/user/installing.html#install-from-source)

Try running this command to enable extra repositories for RHEL 10:
```bash
sudo subscription-manager repos --enable codeready-builder-for-rhel-10-x86_64-rpms
```

1. Clone the repository at [https://github.com/Guake/guake.git](https://github.com/Guake/guake.git).
```bash
git clone https://github.com/Guake/guake.git
```
2. `cd` into the directory that you cloned the repository into.
3. To install dependencies, try to run this command:
```bash
./scripts/bootstrap-dev-fedora.sh run make
```
> There is also a `debian` and an `arch` sh file that you can use as opposed to `fedora`.
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
- `keybinder3`
- `libwnck`

###  Packages needed for making guake
- `gettext`
- `gsettings-desktop-schemas`
- `make`
- `pandoc`

### Packages needed for development
- `dconf-editor`
- `glade`
- `poedit`
- `gnome-tweak-tool`

### Optional packages for execution
- `libutempter`
- `numix-gtk-theme`

The following dependencies were not found on RHEL 10.0:
- `keybinder3`
- `libwnck`
- `glade`
- `poedit`
- `numix-gtk-theme`

You will need to install `keybinder-3.0` from source if you do not have it.

To install `keybinder-3.0` from source, you will need to install the following dependencies from your package manager:
- `gnome-common`
- `gtk-doc`
- `gobject-introspection-devel`
- `gtk3-devel`
- `libappindicator-gtk3-devel`

Then, clone [https://github.com/kupferlauncher/keybinder](https://github.com/kupferlauncher/keybinder).
Then, `cd` into `keybinder` and run this:
```bash
./autogen.sh --libdir /usr/local/lib64
```

Then, run `make`:
```bash
make
```

Then, run `sudo make install`:
```bash
sudo make install
```



