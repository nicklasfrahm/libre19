from euclid3 import Point2
from math import ceil, sin, cos, pi


def deg2rad(deg):
    return pi * (deg / 180)


def arc2d(center=Point2(), r=1, start_deg=0, stop_deg=90, segments=512):
    start = deg2rad(start_deg)
    stop = deg2rad(stop_deg)
    span = stop - start

    steps = ceil(segments * abs(span) / (2 * pi))
    step = span / steps

    return [
        Point2(
            center.x + cos(start + step * i) * r,
            center.y + sin(start + step * i) * r,
        )
        for i in range(steps + 1)
    ]
