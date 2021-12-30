"""
An assembly of all the components of the network stack.
"""
from solid import OpenSCADObject, cube
from solid.objects import translate, color
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19o

# import netstack_v0_psu_case
import netstack_v0_switch_chassis

# Mounting bracket overlap.
MBO = 10

# # Create solid based on the desired appliance size.
X = 400
Y = 150
Z = rxxu(1)
OX = (r19o(1) - X) / 2
solid = combine(
    cube([X, Y, Z]),
    translate([OX, 0, 0]),
)

# Create rack mounting rails.
RX = rxxr(1)
RY = rxxr(1)
RZ = rxxu(4)
rail = combine(
    cube([RX, RY, RZ]),
    color("#333"),
)
solid += combine(
    rail,
    translate([0, MBO, 0]),
)
solid += combine(
    rail,
    translate([r19o(1) - rxxr(1), MBO, 0]),
)

# Add switch chassis.
solid += combine(
    netstack_v0_switch_chassis.obj(),
    color("#ef5350"),
    translate([OX, 0, rxxu(1)]),
)
solid += combine(
    netstack_v0_switch_chassis.obj(),
    color("#ef5350"),
    translate([OX + 200, 0, rxxu(1)]),
)

# # Add mouting pads.
# MX = r19o(1)
# MY = MBO
# MZ = Z
# mount = combine(
#     cube([MX, MY, MZ]),
#     translate([(X - MX) / 2, 0, 0]),
# )
# solid += mount

# # Add switch chassis.
# SCX = 190
# SCY = Y
# SCZ = rxxu(2)
# solid -= combine(
#     cube([SCX, SCY + 2, SCZ + 2]),
#     translate([110, -1, -1]),
# )
# solid += combine(
#     netstack_v0_switch_chassis.obj(),
#     color("#666"),
#     translate([110, 0, 0]),
# )

# # Create slot for power supply.
# PX = 40
# PY = Y + 2
# PZ = 70
# solid -= combine(
#     cube([PX, PY, PZ]),
#     translate([MBO, -1, MBO]),
# )
# solid += combine(
#     netstack_v0_psu_case.obj(),
#     color("#ef5350"),
#     rotate(90, [0, 1, 0]),
#     translate([MBO, 0, PZ + MBO]),
# )

# # Create slot for chassis management controller.
# CX = 40
# CY = Y + 2
# CZ = 70
# solid -= combine(
#     cube([CX, CY, CZ]),
#     translate([PX + MBO * 2, -1, MBO]),
# )
# solid += combine(
#     netstack_v0_psu_case.obj(),
#     color("#ef5350"),
#     rotate(90, [0, 1, 0]),
#     translate([MBO, 0, PZ + MBO]),
# )

# # Create slots for network switches.
# SX = 170
# SY = Y + 2
# SZ = 30
# switch = cube([SX, SY, SZ])
# for i in range(2):
#     solid -= combine(
#         switch,
#         translate([MBO * 4 + PX + CX, -1, MBO + SZ * i + MBO * i]),
#     )
#     solid += combine(
#         netstack_v0_switch_case.obj(),
#         color("#66bb6a"),
#         translate([MBO * 4 + PX + CX, 0, MBO + SZ * i + MBO * i]),
#     )

# # Create slot for network router.
# RX = 80
# RY = 80
# RZ = 25
# router = combine(
#     cube([RX, RY + 1, RZ]),
#     translate([X - RX - MBO, -1, MBO]),
# )
# solid -= router

# # Create slot for fan.
# FX = 80
# FY = 80
# FZ = 25
# fan = combine(
#     cube([FX, FY + 1, FZ]),
#     translate([X - FX - MBO, -1, Z - FZ - MBO]),
# )
# solid -= fan


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
