# Cremini

Cremini is an open-source blade server. It is a combination of mechanical and electronic components, which are managed by an open-source firmware to allow for infrastructure automation.

## Introduction

The mechanical target platform is a 19-inch rack. You may find a comparison of a 10 inch and a 19 inch rack in [this graphic][img-10-vs-19-inch].

### Network stack

One part of the project is a network stack, which provides a top of rack L3 router, network switches and power. Below, you may find a list of all final components and a picture of the current state.

- [x] Rack mount chassis
  - [x] Appliance layout and size constraints
  - [x] Compatibility concept with 10-inch half-rack
  - [ ] Splitting into 3D-printable components
- [x] Power supply
  - [x] Compatibile with [YOUMILE AC-DC 12V6A][amazon-psu-youmile] or [ANGEEK AC-DC 12V6A][amazon-psu-angeek]
  - [ ] Case for **DIY AC-DC 12V5A** power supply
  - [ ] Case for **X115-Y65-Z40** power supplies
- [ ] Network switches
  - [ ] Compatibility with TP-LINK SG108E and NETGEAR GS308E
  - [ ] Case for any 8-port switch
- [ ] Chassis management
  - [ ] Schematic for WT32-ETH01
  - [ ] [Veroboard][wikipedia-veroboard] layout
  - [ ] Firmware for WT32-ETH01
  - [ ] Case for chassis management unit
- [x] Router and firewall
  - [x] Traffic management via [nftables][wiki-nftables]
  - [ ] Case for [Seeed compute module router][seeed-cm4router]

![Network stack CAD preview][img-netstack]

## Development

This section describes how the different components are developed.

### Mechanical design

This project uses [SolidPython][github-solidpython] and [OpenSCAD][website-openscad] for its mechanical design, because it makes it possible to easily create scripts that can be tracked in git. Additionally, the entire CAD workflow can be automated.

- [x] SCAD code generation via `make netstack_v0_assembly.scad`
- [x] STL file generation via `make netstack_v0_assembly.stl`
- [ ] Automatic deployment of STL files to [Thingiverse][thingiverse]
- [ ] GCODE generation, possibly via [CURA engine][reddit-cura-cli]

## Attributions

Some files in this directory were vendored from [Thingiverse][website-thingiverse]. Please find the original creators below.

- [2.5 inch drive tray `mcad/vendor/proliant_tray_2in.stl`](https://www.thingiverse.com/thing:4241436) by [Ian Glen](https://www.thingiverse.com/codethatthinks/designs)
- [3.5 inch drive tray `mcad/vendor/proliant_tray_3in.stl`](https://www.thingiverse.com/thing:4656921) by [Philipp losansky](https://www.thingiverse.com/bluebeardking/designs)

## License

This project is licensed under the terms of the [MIT license][file-license].

[file-license]: ./LICENSE.md
[img-netstack]: ./docs/netstack_v0_assembly.png
[img-10-vs-19-inch]: https://upload.wikimedia.org/wikipedia/commons/8/84/19_inch_vs_10_inch_rack_dimensions.svg
[github-solidpython]: https://github.com/SolidCode/SolidPython
[website-openscad]: https://openscad.org/
[reddit-cura-cli]: https://www.reddit.com/r/Cura/comments/kxz6li/does_cura_have_any_sort_of_cli/
[amazon-psu-youmile]: https://www.amazon.de/dp/B07TZY73H6
[amazon-psu-angeek]: https://www.amazon.de/dp/B07KPK525R
[wikipedia-veroboard]: https://en.wikipedia.org/wiki/Veroboard
[wiki-nftables]: https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F
[seeed-cm4router]: https://www.seeedstudio.com/Rapberry-Pi-CM4-Dual-GbE-Carrier-Board-p-4874.html
[website-thingiverse]: https://www.thingiverse.com
