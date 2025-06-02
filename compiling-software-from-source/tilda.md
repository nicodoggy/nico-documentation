# `tilda` compile instructions

[online documentation](https://github.com/lanoxx/tilda/blob/master/HACKING.md)

<hr />

> Note: I highly recommend following the instructions in [_enabling-extra-packages.md](_enabling-extra-packages.md) as they make getting dependencies easier.

<hr />

## Dependencies (actual package names in `yum`)

### Dependencies for RHEL
- `git`
- `automake`
- `dh-autoreconf`
- `libconfuse-devel`
- `vte291-devel` (if you have a `vte3-devel`, use that)
- `gtk3-devel`
- `glib2-devel`
- `gettext-devel`
- `pcre2-devel`
- `pkgconf-pkg-config`

Try running this to install these dependencies for RHEL.
```bash
sudo yum install git automake dh-autoreconf libconfuse-devel vte291-devel gtk3-devel glib2-devel gettext-devel pcre2-devel pkgconf-pkg-config
```

#### The following dependencies do not seem to be relevant to RHEL, but they may be useful for Ubuntu or Debian.
- `autotools-dev`
- `debhelper`
- `libgtk-3-dev`

### Here is the list of dependencies according the Github repository (not all of these will necessarily exist).

#### On Ubuntu based systems:
- `git`
- `dh-autoreconf`
- `autotools-dev`
- `debhelper`
- `libconfuse-dev`
- `libgtk-3-dev`
- `libpcre2-dev`
- `libvte-2.91-dev`
- `pkg-config`

#### On Fedora:
- `git`
- `automake`
- `libconfuse-devel`
- `vte3-devel`
- `gtk3-devel`
- `glib-devel`
- `gettext-devel`

<hr />

See the [online documentation](https://github.com/lanoxx/tilda/blob/master/HACKING.md) for further instructions.
