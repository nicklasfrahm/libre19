from solid import *
from euclid3 import *
from lib.utils import build, combine
import netstack_v0_psu_case
import netstack_v0_tplink_sg108e_case

## Static design parameters. All units in mm.
# Define outside dimensions.
x = 222
y = 140
z = 88.9
# Define switch dimensions.
sx = 162
sy = 150
sz = 28
# Define fan dimensions.
fx = 25
fy = 80
fz = 80
# Define PSU dimensions.
px = 29
py = 150
pz = 62
# Define router dimensions.
rx = 79
ry = 70
rz = 24

## Tunable parameters.
# Wall thickness.
# TODO: Replace with extrusion width ew = 0.4.
wt = 2
# Offsets.
ox = 1

frame = cube([x, y, z])

switch = cube([sx, sy + 1, sz])
netgear = translate([px + wt * 1.5, -1, wt])(switch)

router = cube([rx, ry + 1, rz])
manager = translate([px + wt * 2 + ox, -1, z - rz - wt])(router)
seeed = translate([px + rx + wt * 3 + ox, -1, z - rz - wt])(router)

fan = combine(
    cube([fx, fy + 1, fz]),
    translate([x - fx - 1, -1, z - fz - wt]),
)

# Assemble TP-Link network switch.
tplink_slot = combine(
    cube([sx, sy + 1, sz]),
    translate([px + wt * 1.5, -1, sz + wt * 2]),
)
tplink_case = combine(
    netstack_v0_tplink_sg108e_case.obj(),
    color("#66bb6a"),
    translate([px + wt * 1.5, 0, sz + wt * 2]),
)

# Assemble power supply.
psu_slot = combine(
    cube([px, py + 1, pz]),
    translate([wt / 2, -1, 10 + wt]),
)
psu_case = combine(
    netstack_v0_psu_case.obj(),
    color("#ef5350"),
    rotate(180, [0, 0, 1]),
    rotate(90, [0, 1, 0]),
    translate([wt / 2, 110, 10 + wt]),
)


def obj():
    return union()(
        difference()(
            frame,
            tplink_slot,
            psu_slot,
            netgear,
            fan,
            manager,
            seeed,
        ),
        psu_case,
        tplink_case,
    )


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
