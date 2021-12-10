from solid import *
from euclid3 import *
from lib.utils import build, combine

## Tunable design parameters.
# Extrusion width.
ew = 0.4
# Handle thickness.
ht = 5

## Static design parameters. All units in mm.
# Define perimeter dimensions.
x = 162
y = 150
z = 28

# Define switch dimensions.
sx = 158
sy = 101
sz = 26

body = cube([x, y, z])

# Create pocket for network switch.
body -= combine(
    cube([x - 6 * ew, 101 + ew * 1.5, 1 + z - ew * 5]),
    translate([ew * 3, ew * 10, ew * 5]),
)

# Create opening for ethernet ports.
body -= combine(
    cube([x - ht * 2, ew * 10 + 2, z - ew * 15]),
    translate([ht, -1, ew * 10]),
)


def obj():
    return body


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
