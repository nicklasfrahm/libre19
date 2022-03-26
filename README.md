# Libre19 🔩

Libre19 is an open hardware form factor for 10-inch network shelves and 19-inch server racks. It is inspired by the [Open19][website-open19] project, but not affiliated with or officially endorsed by Open19 in any way.

You may find a graphical comparison of a 10-inch and a 19-inch rack in [this graphic][img-10-vs-19-inch].

## Features ✨

- **Simple adoption**  
  Libre19 is designed to be easily adopted. Hence it only strictly defines mechanical target dimensions.

- **Flexible connectors**  
  Open19 introduces specialized connectors for networking and power distribution. Although this is great for new deployments, it's not very useful for custom-built, highly-specialized or prototype hardware platforms.

- **Small form factor**  
  Libre19 is designed to be small. It therefore deliberately discourages the use of very deep equipment.

- **10-inch network chassis support**  
  Because of its small form factor, Libre19 also supports 10-inch network shelves.

## Use cases 💡

- **Usage of refurbished or legacy hardware**  
  Most old hardware is hard to integrate with Open19, because Open19 requires the usage of specialized connectors for networking and power distribution. Libre19 only provides a modular 19-inch form factor and is thus fully compatible.

- **Homelabs and small to medium enterprises**  
  Libre19 aims to provide a platform that bridges the gap between public-cloud-scale data centers and DIY hardware assemblies in homelabs.

## Specification 📐

_To be defined; brick, chassis._

## Development 🚧

This project uses [SolidPython][github-solidpython] and [OpenSCAD][website-openscad] for its mechanical design, because it makes it possible to easily create scripts that can be tracked in Git. Additionally, the entire CAD workflow can be automated.

- [x] SCAD code generation via `make libre19_10in_1u.scad`
- [x] STL file generation via `make libre19_10in_1u.stl`
- [ ] Automatic deployment of STL files to [Thingiverse][website-thingiverse]
- [ ] GCODE generation, possibly via [CURA engine][reddit-cura-cli]

## License 📄

This project is and will always be licensed under the terms of the [MIT license][file-license].

[website-open19]: https://open19.org/
[file-license]: ./LICENSE.md
[img-10-vs-19-inch]: https://upload.wikimedia.org/wikipedia/commons/8/84/19_inch_vs_10_inch_rack_dimensions.svg
[github-solidpython]: https://github.com/SolidCode/SolidPython
[website-openscad]: https://openscad.org/
[reddit-cura-cli]: https://www.reddit.com/r/Cura/comments/kxz6li/does_cura_have_any_sort_of_cli/
[website-thingiverse]: https://www.thingiverse.com
