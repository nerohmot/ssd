# <ins>C<ins>onda <ins>P<ins>roxy <ins>P<ins>rocess (cpp)

This is one of the two types of processes that `ssd` (or actually `ssp`) can spin up.

As the name indicates, this process is the local proxy (read: intermediate) for the [spyder-ide](https://www.spyder-ide.org/) (V5 onwards) that runs 
anywhere to administer the conda environment(s) that are not excluded by [ssd.conf](/src/ssd/ssd_conf.md) 

The process will be created as `user`, and is a detached process, meaning that if `ssd` (and thus `ssp`) goes down, this process will **NOT** go down too!
