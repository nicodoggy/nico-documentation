# keybinder 3

To install `keybinder-3.0` from source, you will need to install the following dependencies from your package manager:

- `gnome-common`
- `gtk-doc`
- `gobject-introspection-devel`
- `gtk3-devel`
- `libappindicator-gtk3-devel`

```bash
sudo yum install gnome-common gtk-doc gobject-introspection-devel gtk3-devel libappindicator-gtk3-devel 
```

Then, clone [https://github.com/kupferlauncher/keybinder](https://github.com/kupferlauncher/keybinder).

Then, `cd` into `keybinder` and run this:

```bash
./autogen.sh --prefix=/usr --libdir=/usr/lib64
```
> You need the `--prefix=/usr` and `--libdir=/usr/lib64` because otherwise it might be put in the wrong directory and not be recognized by `guake` and possibly other apps.


Then, run `make`:
```bash
make
```

Then, run `sudo make install`:
```bash
sudo make install
```
