# Hardware 🔩

This repository contains a variety of hardware components that I use to deploy my homelab.

The mechanical target platform is either a 10-inch half-rack or a full-width 19-inch rack depending on the size of the site. You may find a comparison of a 10-inch and a 19-inch rack in [this graphic][img-10-vs-19-inch].

## Components 📦

- [2.5-inch drive tray for HP Proliant DL180 G6][file-drive-tray-2in]
- [Network stack][docs-network-stack]

## Development 🚧

This section describes how the different components are developed.

### Mechanical design 📐

This project uses [SolidPython][github-solidpython] and [OpenSCAD][website-openscad] for its mechanical design, because it makes it possible to easily create scripts that can be tracked in Git. Additionally, the entire CAD workflow can be automated.

- [x] SCAD code generation via `make netstack_v0_assembly.scad`
- [x] STL file generation via `make netstack_v0_assembly.stl`
- [ ] Automatic deployment of STL files to [Thingiverse][website-thingiverse]
- [ ] GCODE generation, possibly via [CURA engine][reddit-cura-cli]

## Attributions ❤️

Some files in this repository were vendored from [Thingiverse][website-thingiverse]. Please find the original creators below.

- [2.5 inch drive tray](https://www.thingiverse.com/thing:4241436) by [Ian Glen](https://www.thingiverse.com/codethatthinks/designs)  
  `mcad/vendor/proliant_tray_2in.stl`

## License 📄

This project is and will always be licensed under the terms of the [MIT license][file-license].

[file-license]: ./LICENSE.md
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
[file-drive-tray-2in]: ./mcad/src/dl180_g6_tray_2in.py
[docs-network-stack]: ./docs/netstack.md
