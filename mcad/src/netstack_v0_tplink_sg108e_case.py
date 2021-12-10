from solid import *
from euclid3 import *
from lib.utils import build, combine

## Tunable design parameters.
# Wall thickness.
wt = 2
# Linear tolerance for 3D printing.
ltol = 0.25
# Handle thickness.
ht = 5

## Static design parameters. All units in mm.
# Define perimeter dimensions.
x = 163
y = 150
z = 28

# Define switch dimensions.
sx = 158
sy = 101
sz = 26

body = cube([x, y, z])

# Create space for network switch.
body -= combine(
    cube([x - wt * 1.6, sy + wt * 2 + 0.6, 1 + z - wt]),
    translate([wt * 0.8, wt * 2, wt]),
)

# Create opening for ethernet ports.
body -= combine(
    cube([x - ht * 2, wt * 2 + 2, z - wt * 3]),
    translate([ht, -1, wt * 2]),
)


def obj():
    return body


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
