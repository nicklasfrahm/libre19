from solid import *
from solid.utils import *
from euclid3 import *

from lib.utils import combine, build
from lib.sketch import arc2d

## Tunable design parameters.
# Wall thickness.
wt = 2
# Linear tolerance for 3D printing.
ltol = 0.25
# Handle thickness.
ht = 5

## Static design parameters. All units in mm.
# Define perimeter dimensions.
x = 62
y = 110
z = 29

# C14 socket.
c14x = 31 + ltol
c14z = 24 + ltol
c14 = combine(
    cube([c14x, wt * 2 + 2, c14z]),
    hole(),
    translate([(x - c14x) / 2, -1, wt + 1.5]),
)

# Basic case without special features.1
box = cube([x, y, z])
cutout = combine(
    cube([x - wt * 2, y - wt * 3, z]),
    translate([wt, wt * 2, wt]),
)
case = box - cutout

# Support to lock C14 connector in place.
sx = 25
sy = 5
sz = 1.5
support = combine(
    cube([sx, sy, sz]),
    translate([(x - sx) / 2, wt * 2, wt]),
)

# Notch to lock PCB in place.
noy = wt * 2 + 98
notch = combine(
    cube([x, y - noy, wt * 4]),
    translate([0, noy, 0]),
)

# Handle for removal from rack assembly.
handle = combine(
    polygon(
        [
            Point2(0, 0),
            Point2(ht, 0),
            *arc2d(Point2(ht * 2, -ht * 2), r=ht, start_deg=180, stop_deg=270),
            *arc2d(Point2(x - ht * 2, -ht * 2), r=ht, start_deg=270, stop_deg=360),
            Point2(x - ht, 0),
            Point2(x, 0),
            *arc2d(Point2(x - ht * 2, -ht * 2), r=ht * 2, start_deg=360, stop_deg=270),
            *arc2d(Point2(ht * 2, -ht * 2), r=ht * 2, start_deg=270, stop_deg=180),
        ],
    ),
    linear_extrude(ht),
    rotate(180, [0, 0, 1]),
    translate([x, y, 0]),
)

# Hole for power LED.
ledd = 3.3
led = combine(
    cylinder(r=ledd / 2, h=wt * 2 + 2),
    hole(),
    rotate(-90, [1, 0, 0]),
    translate([x - wt * 4, y - wt - 1, z - wt * 4]),
)

# Outlet for 12V power cables.
od = 4
outlet = combine(
    cylinder(r=od / 2, h=wt * 2 + 2),
    hole(),
    rotate(-90, [1, 0, 0]),
    translate([x - wt * 4, -1, z - wt * 4]),
)


def obj():
    return color("violet")(
        union()(
            case,
            support,
            notch,
            handle,
            c14,
            led,
            outlet,
        )
    )


# Boilerplate code to exportthe file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
