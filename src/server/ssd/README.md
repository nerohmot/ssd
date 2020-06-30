# <ins>**S**</ins>pyder <ins>**S**</ins>pinner <ins>**D**</ins>aemon (ssd)

`ssd` wraps the <ins>**S**</ins>pyder <ins>**S**</ins>pinner <ins>**P**</ins>rocess ([ssp](/src/ssp)) in a Daemon/Service for each of the following OS-es:

- Windows
- Linux
- MacOS

The operating system determins the location of:

- `ssd.conf` file ➜ the configuration file, described [here](/src/ssd/ssd_conf.md)
  - Windows : TBD
  - Linux : `/etc/ssd.conf`
  - MacOS : `/etc/ssd.conf`
- `ssd.pid` file ➜ the pid file for ssd proper, described [here](/src/ssd/ssd_pid.md)
  - Windows :
  - Linux : `/var/run/ssd.pid`
  - MacOS :
- `ssd.pids` file ➜ the pid of the sped up processes, described [here](/src/ssd/ssd_pids.md)
  - Windows :
  - Linux : `/var/run/ssd.pids`
  - MacOS :
