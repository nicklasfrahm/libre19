from solid import *
from solid.utils import *
from euclid3 import *
from lib.utils import build, combine
import netstack_v0_psu_case

## Static design parameters. All units in mm.
# Define outside dimensions.
x = 225
y = 140
z = 88.9
# Define switch dimensions.
sx = 160
sy = 150
sz = 28.5
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
wt = 2
# Offsets.
ox = 1

frame = cube([x, y, z])

switch = cube([sx, sy + 1, sz])
tplink = translate([px + wt * 2 + ox, -1, wt])(switch)
netgear = translate([px + wt * 2 + ox, -1, sz + wt * 2])(switch)

router = cube([rx, ry + 1, rz])
manager = translate([px + wt * 2 + ox, -1, z - rz - wt])(router)
seeed = translate([px + rx + wt * 3 + ox, -1, z - rz - wt])(router)

fan = translate([x - fx - wt, -1, z - fz - wt])(cube([fx, fy + 1, fz]))

psu_cutout = translate([wt, -1, wt])(cube([px, py + 1, pz]))
psuv0 = combine(
    netstack_v0_psu_case.obj(),
    color("#ef5350"),
    rotate(180, [0, 0, 1]),
    rotate(90, [0, 1, 0]),
    translate([wt, 110, wt]),
)


def obj():
    return difference()(
        frame,
        tplink,
        netgear,
        fan,
        psu_cutout,
        manager,
        seeed,
    )


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj() + psuv0, __file__)
