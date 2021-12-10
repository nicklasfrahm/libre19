"""
A case for a 1000BASE-T network switch. Compatibility tested with:
- NETGEAR GS308E
- TP-LINK SG108E
"""
from solid import cube, translate, OpenSCADObject
from lib.utils import build, combine

## Tunable design parameters.
# Extrusion width.
EW = 0.4
# Layer height.
LH = 0.15
# Handle thickness.
HT = 12 * EW


def dim_xy(dim: float) -> float:
    """
    Given a dimension in the xy-plane, this function will
    round down to the next multiple of the extrusion width.
    """
    # Add small value to reduce risk of the remainder being zero.
    dim += 1e-10
    return (dim // EW) * EW


def dim_z(dim: float) -> float:
    """
    Given a dimension along the z-axis, this function will
    round down to the next multiple of the layer height.
    """
    # Add small value to reduce risk of the remainder being zero.
    dim += 1e-10
    return (dim // LH) * LH


## Static design parameters. All units in mm.
# Define perimeter dimensions.
X = 162
Y = 150
Z = 28

# Define switch pocket dimensions.
SX = 158
SY = 101.25
SZ = 26.1
SZB = 27.2

# Define body solid.
body: OpenSCADObject = cube([X, Y, Z])

# Create pocket for network switch.
SXT = dim_xy(SX) + EW * 2
SYT = dim_xy(SY) + EW * 2
body -= combine(
    cube([SXT, SYT, SZ + 2]),
    translate([(X - SXT) / 2, EW * 10, dim_z(Z - SZ)]),
)

# Create opening for ethernet ports.
body -= combine(
    cube([X - HT * 2, EW * 10 + 2, dim_z(Z - LH * 24)]),
    translate([HT, -1, LH * 18]),
)

# Create a support for the ethernet port opening.
SUPX = EW * 5
body += combine(
    cube([SUPX, EW * 10, Z]),
    translate([(X - SUPX) / 2, 0, 0]),
)

# TODO: Add handles.
# TODO: Add power input port.
# TODO: Add pocket for NETGEAR switch.
# TODO: Add mount for DC-DC converter.


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return body


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
