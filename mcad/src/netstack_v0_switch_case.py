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
X = 170
Y = 150
Z = 30

# Define switch pocket dimensions.
SX = 158
SY = 101.25
SZ = 26.15

# Define body solid.
body: OpenSCADObject = cube([X, Y, Z])

# Create pocket for network switch.
SXT = dim_xy(SX) + EW * 2
SYT = dim_xy(SY) + EW * 2
SZT = dim_z(Z - SZ)
body -= combine(
    cube([SXT, SYT, SZ + 2]),
    translate([(X - SXT) / 2, EW * 10, SZT]),
)

# Create a pocket to account for NETGEAR SG308E sheet metal fold.
SMY = 11
SMZ = 27.45
SMYT = dim_xy(SMY) + EW * 2
SMZT = dim_z(Z - SMZ)
body -= combine(
    cube([SXT, SMYT, SMZ]),
    translate([(X - SXT) / 2, SYT + EW * 10 - SMYT, SMZT]),
)

# Create opening for ethernet ports.
SEZ = dim_z(Z - LH * 24)
body -= combine(
    cube([X - HT * 2, EW * 10 + 2, SEZ]),
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
