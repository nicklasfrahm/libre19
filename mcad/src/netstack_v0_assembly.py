"""
An assembly of all the components of the network stack.
"""
from solid import OpenSCADObject, cube
from solid.objects import translate, rotate, color
from lib.utils import build, combine
from lib.units import rxxu, r19o
import netstack_v0_psu_case
import netstack_v0_switch_case
import netstack_v0_switch_chassis

## Tunable design parameters.
# Wall thickness.
WT = 10

# Create solid based on the desired appliance size.
X = 400
Y = 150
Z = rxxu(2)
solid = combine(
    cube([X, Y, Z]),
)

# Add mouting pads.
MX = r19o(1)
MY = WT
MZ = Z
mount = combine(
    cube([MX, MY, MZ]),
    translate([(X - MX) / 2, 0, 0]),
)
solid += mount

# Add switch chassis.
SCX = 190
SCY = Y
SCZ = rxxu(2)
solid -= combine(
    cube([SCX, SCY + 2, SCZ + 2]),
    translate([110, -1, -1]),
)
solid += combine(
    netstack_v0_switch_chassis.obj(),
    color("#666"),
    translate([110, 0, 0]),
)

# Create slot for power supply.
PX = 40
PY = Y + 2
PZ = 70
solid -= combine(
    cube([PX, PY, PZ]),
    translate([WT, -1, WT]),
)
solid += combine(
    netstack_v0_psu_case.obj(),
    color("#ef5350"),
    rotate(90, [0, 1, 0]),
    translate([WT, 0, PZ + WT]),
)

# Create slot for chassis management controller.
CX = 40
CY = Y + 2
CZ = 70
solid -= combine(
    cube([CX, CY, CZ]),
    translate([PX + WT * 2, -1, WT]),
)
solid += combine(
    netstack_v0_psu_case.obj(),
    color("#ef5350"),
    rotate(90, [0, 1, 0]),
    translate([WT, 0, PZ + WT]),
)

# Create slots for network switches.
SX = 170
SY = Y + 2
SZ = 30
switch = cube([SX, SY, SZ])
for i in range(2):
    solid -= combine(
        switch,
        translate([WT * 4 + PX + CX, -1, WT + SZ * i + WT * i]),
    )
    solid += combine(
        netstack_v0_switch_case.obj(),
        color("#66bb6a"),
        translate([WT * 4 + PX + CX, 0, WT + SZ * i + WT * i]),
    )

# Create slot for network router.
RX = 80
RY = 80
RZ = 25
router = combine(
    cube([RX, RY + 1, RZ]),
    translate([X - RX - WT, -1, WT]),
)
solid -= router

# Create slot for fan.
FX = 80
FY = 80
FZ = 25
fan = combine(
    cube([FX, FY + 1, FZ]),
    translate([X - FX - WT, -1, Z - FZ - WT]),
)
solid -= fan


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
