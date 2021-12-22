"""
A case for a 1000BASE-T network switch. Compatibility tested with:
- NETGEAR GS308E
- TP-LINK SG108E
"""
from solid import cube, cylinder, translate, OpenSCADObject
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
SPX = dim_xy(158) + EW * 10
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

# Create a pocket to account for NETGEAR SG308E sheet metal fold.
SFY = 11
SFZ = Z - 27.45
SFYT = dim_xy(SFY) + EW * 2
SFZT = dim_z(SFZ)
solid -= combine(
    cube([SPX, SFYT, Z]),
    translate([(X - SPX) / 2, EW * 10 + SPY - SFYT, SFZT]),
)

# Create space for wiring.
SWZ = dim_z(SPZT + 5)
solid -= combine(
    cube([SPX, Y - EW * 10 - (X - SPX) / 2, Z]),
    translate([(X - SPX) / 2, EW * 10, SWZ]),
)

# Create pocket for DC-DC converter.
SCX = 43.05
SCY = 21.18
SCZ = 5
SCXT = dim_xy(SCX) + EW
SCYT = dim_xy(SCY) + EW
SCZT = dim_z(5)
solid -= combine(
    cube([SCXT, SCYT, Z]),
    translate([(X - SCXT) / 2, EW * 10 + SPY + EW * 10, SCZ]),
)

# Add power input port.
PIX = 24.2
PIY = 6.55
PIZ = 3.8
PIOZ = 1.5
PIXT = dim_xy(PIX) + EW * 2
PIYT = dim_xy(PIY) + EW * 2
PIZT = dim_z(PIZ) + LH
PIOZT = dim_z(SWZ - PIOZ)
PISD = 1
solid -= combine(
    cube([PIXT, PIYT + 1, PIZT]),
    translate([(X - SPX) / 2 + 30, Y - PIYT + 1, PIOZT]),
)
screw = combine(
    cylinder(r=2 / 2, h=9 + 2),
)
solid -= combine(
    screw,
    translate([(X - SPX) / 2 + 30 + 10.3, Y - 8, SWZ - 11 + 1]),
)
solid -= combine(
    screw,
    translate([(X - SPX) / 2 + 30 + 10.3 + 7.6, Y - 8, SWZ - 11 + 1]),
)

# Add handles to solid.
HL = 50
solid += handle(HL)
solid += combine(
    handle(HL),
    translate([X - HL, 0, 0]),
)


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
