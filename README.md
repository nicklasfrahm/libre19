# Cremini

Cremini is an open-source blade server. It is a combination of mechanical, electronic components, which are managed by an open-source firmware to allow for infrastructure automation.

## Introduction

The mechanical target platform is a 10 inch rack, sometimes also referred to as a _half-width rack_. You may find a comparison of a 10 inch and a 19 inch rack in [this graphic][img-10-vs-19-inch].

### Network stack

One part of the project is a network stack, which provides a top of rack L3 router, network switches and power. Below, you may find a list of all final components and a picture of the current state.

- [x] Refurbished old 60W 12VDC power supply with custom case
- [ ] TP-LINK SG108E 1000BASE-T smart L2 network switch with case
- [ ] NETGEAR GS308E 1000BASE-T managed L2 network switch with case
- [ ] WT32-ETH01 chassis, power and thermal management with case
- [ ] Seeed Dual-Gigabit NIC carrier board for compute module 4 with case

![Network stack CAD preview][img-netstack]

## Development

This section describes how the different components are developed.

### Mechanical design

This project uses [SolidPython][github-solidpython] and [OpenSCAD][website-openscad] for its mechanical design, because it makes it possible to easily create scripts that can be tracked in git. Additionally, the entire CAD workflow can be automated.

- [x] SCAD code generation via `make netstack_v0_assembly.scad`
- [x] STL file generation via `make netstack_v0_assembly.stl`
- [ ] GCODE generation, possibly via [CURA engine][reddit-cura-cli]

## License

This project is licensed under the terms of the [MIT license][file-license].

[file-license]: ./LICENSE.md
[img-netstack]: ./docs/netstack_v0.png
[img-10-vs-19-inch]: https://upload.wikimedia.org/wikipedia/commons/8/84/19_inch_vs_10_inch_rack_dimensions.svg
[github-solidpython]: https://github.com/SolidCode/SolidPython
[website-openscad]: https://openscad.org/
[reddit-cura-cli]: https://www.reddit.com/r/Cura/comments/kxz6li/does_cura_have_any_sort_of_cli/
