# IMPORTANT NOTE

This repository has been folded into the Seed repository and is no longer in use.

# Corepops

A Poplog installation bootstraps itself from a working Poplog executable. This 
repository contains known, working Poplog corepop executables that can be used
for the bootstrapping process. This repository is used by the scripts of the 
Seed repository.

## Naming Convention for Corepop Images

The naming convention is nnn-kk_kk_kk-yyyy_mm_dd.corepop, where:

- nnn is the preference order (smaller before bigger) initially steps of 10 to allow for additions without frequent renumbering. We will need to renumber every so often.
- kk_kk_kk is a kernel number it is known to work on.
- yyyy_mm_dd is the date it was produced.


## Corepop test results

<!--BEGIN COREPOP_TEST_RESULTS-->
| Corepop | Distribution | Version | Pass | Exit code | Logs |
| ------- | ------------ | ------- | ---- | --------- | ---- |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: cb0195af37> | 21.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: d8b40e1d06> | 20.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: a69124dbe0> | 18.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 6aa5b2b382> | 16.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: c01a516d80> | latest | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: f9a496296f> | unstable-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 6c0ee50180> | testing-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 1a0337f6c3> | stable-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 73a8087053> | oldstable-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: a26d0d0b20> | oldoldstable | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 4f99e19201> | 34 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 96ccd2820b> | 33 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 85ce7ef2ae> | 32 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: 88fc013e71> | 8 | :heavy_check_mark: | 0 |  |
| linux/x86_64/010-05_11_12-2021_07_07.corepop | <Container: eab6642bae> | 7 | :heavy_check_mark: | 0 |  |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 3885ab0e95> | 21.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: fe2e31dc98> | 20.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 1936a5e862> | 18.04 | :x: | 1 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found (required by /corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop)<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 0d7d6a79d6> | 16.04 | :x: | 1 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found (required by /corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop)<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 13879b8458> | latest | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: b3788d07d6> | unstable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 142519d140> | testing-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 6ad700d1a6> | stable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 619b5761ee> | oldstable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 1a0403f995> | oldoldstable | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 9b6523cbc7> | 34 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: da080e12ef> | 33 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: a5895e68f8> | 32 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: 77be1b7d28> | 8 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/020-05_08_00-2021_06_24.corepop | <Container: b4a9718129> | 7 | :x: | 1 | <details><summary>details</summary><pre>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: /lib64/libtinfo.so.5: no version information available (required by /corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop)<br>/corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop: /lib64/libm.so.6: version `GLIBC_2.29' not found (required by /corepops/linux/x86_64/020-05_08_00-2021_06_24.corepop)<br></pre></details> |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 3028741383> | 21.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 1390703a88> | 20.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 271c3be66c> | 18.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: b996162540> | 16.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 4bb8498d33> | latest | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: b2bde52471> | unstable-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 123bba6957> | testing-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: c9219c0e81> | stable-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 74cd9a2edb> | oldstable-slim | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 294a3a0880> | oldoldstable | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 4c00a39b8c> | 34 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 1e3e95e59b> | 33 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 24319a45bc> | 32 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 529bcdcca6> | 8 | :heavy_check_mark: | 0 |  |
| linux/x86_64/030-05_04_00-2020_08_22.corepop | <Container: 6fc592fcc7> | 7 | :heavy_check_mark: | 0 |  |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 5a91627516> | 21.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: c2c59ea369> | 20.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 40e94c7d90> | 18.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 7ad3f8e406> | 16.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 225cd1fcf6> | latest | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 1413ddbe31> | unstable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 0cd0f960b7> | testing-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 214971dadc> | stable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: ee83299f3c> | oldstable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 268975ec6a> | oldoldstable | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: cb8a4a7b01> | 34 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 3c4bd8f7b1> | 33 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 5bbd36d4c1> | 32 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: 0fe723f864> | 8 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/040-05_08_00-2021_07_30.corepop | <Container: d3d3f0df9c> | 7 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/040-05_08_00-2021_07_30.corepop: error while loading shared libraries: libXt.so.6: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 83d4c2d356> | 21.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 860dfa4c0f> | 20.04 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 04e47a5d3b> | 18.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 5f3f2dd718> | 16.04 | :heavy_check_mark: | 0 |  |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: c8924566b5> | latest | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 59d8efb212> | unstable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 1d4b7446cd> | testing-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: e4bb6781df> | stable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 0961734f33> | oldstable-slim | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: ab9ca3fefe> | oldoldstable | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: dbcd59b40e> | 34 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 62f487d504> | 33 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 59f77adeea> | 32 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 688f3ec782> | 8 | :x: | 127 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory<br></pre></details> |
| linux/x86_64/050-04_04_00-2020_00_00.corepop | <Container: 11ab0edc88> | 7 | :x: | 0 | <details><summary>details</summary><pre>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: /lib64/libtinfo.so.5: no version information available (required by /corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop)<br>/corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop: /lib64/libtinfo.so.5: no version information available (required by /corepops/linux/x86_64/050-04_04_00-2020_00_00.corepop)<br></pre></details> |
<!--END COREPOP_TEST_RESULTS-->
