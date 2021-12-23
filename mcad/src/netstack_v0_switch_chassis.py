"""
A chassis to hold two network switch cases.
"""
from solid import cube, cylinder, rotate, translate, OpenSCADObject
from solid.utils import forward, up, right
from lib.utils import build, combine
from lib.units import rxxu

## Tunable design parameters.
# Extrusion width.
EW = 0.4
# Layer height.
LH = 0.15
# Handle thickness.
HT = 5
# Wall thickness.
WT = 10

# Define body solid.
X = 190
Y = 150
Z = rxxu(2)
solid = cube([X, Y, Z])

# Create slots for network switches.
SX = 170
SY = Y
SZ = 30
switch = cube([SX, SY + 2, SZ])
for i in range(2):
    solid -= combine(
        switch,
        translate([(X - SX) / 2, -1, WT + i * WT + i * SZ]),
    )

# Create corners for assembly.
CX = X - SX + 2e-2
CY = WT * 2
CZ = Z
corner = combine(
    cube([CX, CY, CZ + 2], center=True),
    up(Z / 2),
)
SR = 2.5 / 2
SH = 10
SYO = -(CY / 2 + SH)
screw = combine(
    cylinder(r=SR, h=CY + 2 * SH),
    rotate(-90, [1, 0, 0]),
)
for i in range(3):
    corner += combine(
        screw,
        translate([5, SYO, 5 + i * SZ + i * 10]),
    )
for i in range(3):
    corner += combine(
        screw,
        translate([-5, SYO, 5 + i * SZ + i * 10]),
    )
solid -= corner
solid -= combine(
    corner,
    forward(Y),
)
solid -= combine(
    corner,
    forward(Y),
    right(X),
)
solid -= combine(
    corner,
    right(X),
)


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
