# <ins>S</ins>pyder <ins>K</ins>ernel <ins>P</ins>rocess (skp)

This is one of the two types of processes that `ssd` (or actually `ssp`) can spin up.

As the name indicates, this process is a wrapper around the [spyder-kernels](https://github.com/spyder-ide/spyder-kernels).

`ssd` (or effectively `ssp`) will spin up this process as a specified `user`, then start the `spyder-kernel` **in** a given conda environment (that is not excluded by the 
[ssd.conf](/src/ssd/ssd_conf.md) file)

`ssp` will send back the connection data (the .json file) to the [spyder-ide](https://www.spyder-ide.org/) in order to achieve seamless remote connection.

The process is a detached, meaning that if `ssd` (and thus `ssp`) goes down, this process will **NOT** go down too!
