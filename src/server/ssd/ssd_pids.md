# ssd.pid<ins>s</ins>

This file contains 1 line for each process that `ssd` (or acctually `ssp`) did sped up.

The format is similar to `ssd.pid` with the addition of the process type (`cpp` or `skp`)

<process_type>:<process_id>:<process_ctime>

- process_type : string, either "cpp" or "skp"
- process_id : unsigned integer
- process_ctime : unsigned integer

eg:

```sh
skp:23456:1593508442
skp:25678:1593509021
cpp:26789:1593509100
```

## Note:
The process creation time is added for addes security.
