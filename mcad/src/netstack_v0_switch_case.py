"""
A case for a 1000BASE-T network switch. Compatibility tested with:
- NETGEAR GS308E
- TP-LINK SG108E
"""
from solid import cube, translate, OpenSCADObject
from lib.utils import build, combine
from lib.features import handle

## Tunable design parameters.
# Extrusion width.
EW = 0.4
# Layer height.
LH = 0.15
# Handle thickness.
HT = 5


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


# Define body solid.
X = 170
Y = 150
Z = 30
solid = cube([X, Y, Z])

# Create pocket for network switch.
SPX = dim_xy(158) + EW * 2
SPY = dim_xy(101.25) + EW * 2
SPZT = dim_z(Z - 26.15)
solid -= combine(
    cube([SPX, SPY, Z + 2]),
    translate([(X - SPX) / 2, EW * 10, SPZT]),
)

# Create opening for ethernet ports.
EX = dim_xy(SPX - EW * 4)
EY = EW * 10 + 2
EZ = dim_z(Z - HT - LH * 10)
EPZ = dim_z(Z - HT - LH)
solid -= combine(
    cube([EX, EY, EZ]),
    translate([(X - EX) / 2, -1, HT]),
)

# Create a support for the ethernet port opening.
SUPX = EW * 5
SUPY = EW * 10
solid += combine(
    cube([SUPX, SUPY, Z]),
    translate([(X - SUPX) / 2, 0, 0]),
)

# Create a pocket to account for NETGEAR SG308E sheet metal fold.
# SMY = 11
# SMZ = 27.45
# SMYT = dim_xy(SMY) + EW * 2
# SMZT = dim_z(Z - SMZ)
# solid -= combine(
#     cube([SXT, SMYT, SMZ]),
#     translate([(X - SXT) / 2, SYT + EW * 10 - SMYT, SMZT]),
# )

# TODO: Add power input port.
# TODO: Add pocket for NETGEAR switch.
# TODO: Add mount for DC-DC converter.

# Add handles to solid.
HT = 50
solid += handle(HT)
solid += combine(
    handle(HT),
    translate([X - HT, 0, 0]),
)


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
