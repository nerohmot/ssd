# <ins>**S**</ins>pyder <ins>**S**</ins>pinner <ins>**P**</ins>rocess (ssp)

`ssp` is the core of the project. It is responsible for the following tasks:

## @Startup
Upon startup, the following tasks will be performed:

- reading the `ssd.conf`config file (location is dependent on OS, determined by SSD)
- verifying if a `ssd.pid` file (location is dependent on OS, tetermined by SSD) exists.
  - Yes --> open it, and see if the pid/ctime mentioned is still running.
    - Yes --> exit
    - No --> remove the `ssd.pid` file and go on as if the `ssd.pid` file didn't exits.  
  - No --> write the (SSD) pid and c-time to the `ssd.pid` file.
- grab a free TCP/IP port and publish itself to the zeroconf network.
- go into 'idle' mode.

## 'idle' mode

The [ssd.conf](/src/ssd/ssd_conf.md) file holds an entry `max_slots` (= maximum number of processes it will spin up).
Each time a CPP or SKP is sped up, SSP is keeping track of the pid & c-time in a `slots` dictionary.
If in the `slots` dictionary a CPP is found, the 'idle' mode will check once every second if the processes still exist.
If in the `slots` dictionary no CPP is found, the 'idle' mode will check once every 10-30 seconds if the processes still exist.

## 'connection' mode

 





- spin up CPP or SKP **DETACHED** **AS** the supplied user **IN** the supplied conda environment.
  - DETACHED --> if SSD/SSP goes down, the already sped up processes (CPP/SKP) will **NOT** go down with SSD/SSP.
as a consequence, all PID's of the sped up processes will be written in the `.pid` file too, this way, if SSD/SSP
goes down, and comes up again, it can proceed where it left off.

  - SSP keeps the pid of the sped up process, and writes it in his `.pid` file too.
  - SPS will return the connection data 

