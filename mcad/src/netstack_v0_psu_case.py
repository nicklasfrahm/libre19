"""
A case for the refurbished power supply of the network stack.
"""
from solid import OpenSCADObject
from solid.objects import cube, cylinder, hole, translate, rotate
from lib.utils import combine, build
from lib.features import handle

## Tunable design parameters.
# Wall thickness.
WT = 2
# Linear tolerance for 3D printing.
TOL = 0.25
# Handle thickness.
HT = 5

# Create solid based on the desired appliance size.
X = 62
Y = 110
Z = 29
solid = cube([X, Y, Z])

# Create opening for C14 connector.
C14X = 31 + TOL
C14Z = 24 + TOL
c14 = combine(
    cube([C14X, WT * 2 + 2, C14Z]),
    translate([(X - C14X) / 2, Y - WT * 2 - 1, WT + 1.5]),
)
solid -= c14

# Create slot for power supply.
psu = combine(
    cube([X - WT * 2, Y - WT * 3, Z]),
    translate([WT, WT, WT]),
)
solid -= psu

# Add support to lock C14 connector in place.
SX = 25
SY = 5
SZ = 1.5
support = combine(
    cube([SX, SY, SZ]),
    translate([(X - SX) / 2, Y - SY - WT * 2, WT]),
)
solid += support

# Add notch to lock PCB in place.
NOY = Y - WT * 3 - 98
notch = combine(
    cube([X, NOY, WT * 4]),
    translate([0, WT, 0]),
)
solid += notch

# Create hole for power LED.
LEDD = 3.3
led = combine(
    cylinder(r=LEDD / 2, h=WT * 2 + 2),
    rotate(-90, [1, 0, 0]),
    translate([WT * 4, -1, Z - WT * 4]),
)
solid -= led

# Outlet for 12V power cables.
OD = 4
outlet = combine(
    cylinder(r=OD / 2, h=WT * 2 + 2),
    hole(),
    rotate(-90, [1, 0, 0]),
    translate([WT * 4, Y - WT * 2 - 1, Z - WT * 4]),
)
solid -= outlet

# Add handle for removal from rack assembly.
solid += handle(X)


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
