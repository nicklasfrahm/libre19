"""
A chassis to hold two network switch cases.
"""
from solid import cube, cylinder, rotate, translate, OpenSCADObject
from solid.utils import forward, up, right
from lib.utils import build, combine
from lib.units import rxxu

# Mounting bracket overlap.
MBO = 10
# Mounting screw hole radius.
MSR = 2.5 / 2
# Mounting screw hole depth.
MSD = 10

# Define body solid.
X = 200
Y = 150
Z = rxxu(1)
solid = cube([X, Y, Z])

# Create slot for network switch.
SX = 163
SY = Y
SZ = 28
solid -= combine(
    cube([SX, SY + 2, SZ]),
    translate([(X - SX) / 2, -1, (Z - SZ) / 2]),
)

# Create slot for foam padding.
FT = 5
FX = SX + FT * 2
FY = SY + FT * 2
FZ = SZ + FT * 2
solid -= combine(
    cube([FX, FY, FZ]),
    translate([(X - FX) / 2, 20, (Z - FZ) / 2]),
)

# Create corners for assembly.
CX = MBO * 2
CY = MBO * 2
CZ = Z
corner = combine(
    cube([CX, CY, CZ + 2], center=True),
    up(Z / 2),
)
MSO = -(CY / 2 + MSD)
screw = combine(
    cylinder(r=MSR, h=CY + 2 * MSD),
    rotate(-90, [1, 0, 0]),
)
for i in range(2):
    corner += combine(
        screw,
        translate([5, MSO, 5 + i * Z - i * 10]),
    )
for i in range(2):
    corner += combine(
        screw,
        translate([-5, MSO, 5 + i * Z - i * 10]),
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

# Add notches to lock switch in place.
NX = (FX - SX) / 2 + 15
NY = 102
for i in range(2):
    solid += combine(
        cube([NX, Y - NY, Z]),
        translate([(X - FX) / 2 + i * (FX - NX), NY, 0]),
    )

# Create slot for back cover.
BX = FX - NX * 2 + 2 * 2
BY = 2
BZ = FZ
solid -= combine(
    cube([BX, BY, BZ]),
    translate([(X - BX) / 2, Y - BY * 2, (Z - FZ) / 2]),
)


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
