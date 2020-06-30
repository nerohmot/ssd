# <ins>**S**</ins>pyder <ins>**S**</ins>pinner <ins>**D**</ins>aemon (ssd)

# Preample

Up to now, in spyder, there is some 'buttox pains' when it comes to:
  1. **Detecting what 'machines' are available in your network**, this is prior to 'connecting' to them, and currently not available.
  2. **Connecting to remote spyder-kernels**, this is available, but it is very manual. (actually almost un-usable for head-less devices).
  3. **Environment(s)** ... If ther is any, they are not 'controlled' from `Spyder`. (Or better yet : the application you are coding for!)

This initial proposal tries to solve thes issues transparantly both remote **and local!** (see notes at end)

# Description (Proposal)

The `ssd` uses [zeroconf](https://github.com/jstasiak/python-zeroconf) to announce it's presence to the zeroconf network.

[Spyder](https://github.com/spyder-ide/spyder) can now easily 'discover' what machines are available (including the local machine)!

When the user identifies the desired target, Spyder contacts the `ssd` (more correctly `ssp`). We need however to suply a `username` and `password`.
It is clear that we don't send the password as clear text, we instead use TSL (standare Python [ssl](https://docs.python.org/3.8/library/ssl.html) library or [pyopenssl](https://www.pyopenssl.org/en/stable/)) to communicate with an `ssd`. TLS from his side needs 'certificates', so the `ssd installer` will create a [self-signed certificate](https://stackoverflow.com/questions/10175812/how-to-create-a-self-signed-certificate-with-openssl) when installing `ssd`.

If more security is desirable, the IT department needs to replace the self-signed certificates by certificates signed by a certified autority.

Spyder can now ask the connected `ssd` to spin up a `cpp` (<ins>**C**</ins>onda <ins>**P**</ins>roxy <ins>**P**</ins>rocess) as the `user` used to connect to `ssd` itself.
`ssd` will do so, and report back the connection info to the just spinned up `cpp`. Spyder connects to the `cpp` and can figure out the avialable environments (for `user`), and, if so desired and configured, administer the conda environment. In the minimal use-case, spyder uses `cpp` to obtain a list of available conda environments for `user`.

Having the available conda environments, Spyder can now ask the connected `ssd` to spin up a `skp` (<ins>**S**</ins>pyder <ins>**K**</ins>ernel <ins>**P**</ins>rocess) as a `user` in a specific `conda environment`. `ssd` will do so and report back the connection data (= the infamous .json file) so that `spyder` can sub-sequently connect auto-magically to the freshley spinned spyder-kernel.

# installation

The installer will ask what needs to be installed if one does `$conda install ssd`.

For the installation of the server side, one needs to supply the root/Administrator password at the command line.

If one does `$conda install -y ssd` it is presumed that both client- and server-side need installation, however as conda is started as non-root/administrator, the installation script thus **will** prompt to supply the root/administrator password even though the '-y' option was provided.

If one does `sudo conda install -y ssd` (Linux/MacOS only), the installation is truely 'silent'.

The server side will install `ssd` in his own 'application environment' with the name `_ssd_` ofcourse accessable by root/Administrator.

[anaconda](https://www.anaconda.com/products/individual), [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [miniforge](https://github.com/conda-forge/miniforge) is thus best installed on systems as ['multi-user'](
https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/admin-multi-user-install.html)

We give `ssd` it's own 'application environment' so that testing only needs to cover the [requirements](/requirements) set forward by `ssd` itself, and not clutter any other environments.

In any case, the `ssd` is started in the following manner:

```sh
conda run -n _ssd_ python ssd
```

# Release

