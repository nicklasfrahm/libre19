"""
A chassis to hold two network switch cases.
"""
from solid import OpenSCADObject, cube, translate
from lib.utils import build, stl, combine

print()
print("Rendering to STL via OpenSCAD CLI may take several")
print("minutes due to STL import! Please be patient!")
print()

original = stl("vendor/proliant_tray_2in.stl")

front = original
front -= combine(
    cube([130, 150, 100]),
    translate([70, 0, 0]),
)


back = original
back -= combine(
    cube([81.5, 150, 100]),
    translate([-10, -10, 0]),
)

# Shorten tray by 1.5mm to make it compatible with G6.
solid = front
solid += combine(
    back,
    translate([-1.5, 0, 0]),
)


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
