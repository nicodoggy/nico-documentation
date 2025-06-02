# Enabling Extra Packages for `RHEL 10`

> Because sometimes, compiling documentation from source just isn't that appealing.

Run the following two commands to get extra repos! **Yay!!!**

```bash
sudo subscription-manager repos --enable codeready-builder-for-rhel-10-x86_64-rpms
```

```bash
subscription-manager repos --enable=rhel-10-for-x86_64-appstream-rpms
```
