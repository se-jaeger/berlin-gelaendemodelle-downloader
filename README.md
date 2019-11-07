
# Download Client for Berlin Geländemodelle

Downloads [Berlins' height information](https://www.stadtentwicklung.berlin.de/geoinformation/landesvermessung/atkis/de/dgm.shtml) (Digitale Geländemodelle – ATKIS DGM - Höheninformationen), compress them on the fly, and create GeoJSON files.


## What means 'Compress'

Compression means tiles, shaped as windows, are averaged. Because one subset of the data is of shape `2000x2000`, the tile size, argument `compress`, have to divide 2000 without remainder.


## Getting Started

WIP


## Features - WIP

- [ ] Write Publish documentation
- [x] Create some output
- [x] Download the whole dataset
- [x] Compress it on the fly (choose tile size (2000 should be divisible by tile size without remainder))
- [x] Keep original data (flag)
- [ ] choose download file data type


## Note

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
