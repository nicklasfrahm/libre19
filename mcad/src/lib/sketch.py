"""
Utilities for creating shapes in 2D sketches.
"""
from math import ceil, sin, cos, pi
from euclid3 import Point2


def deg2rad(deg: float):
    """
    Converts degress to radians.
    """
    return pi * (deg / 180)


def arc2d(center=Point2(), radius=1, start=0, stop=90, segments=512):
    """
    Draws an arc of specified `radius` aroung the given `center` point
    from `start` to `end`, where both are angles given in degrees. The
    resolution of the arc can be adjusted via the segments parameter,
    which sets the number of points on a 360 degree full circle.
    """
    start = deg2rad(start)
    stop = deg2rad(stop)
    span = stop - start

    steps = ceil(segments * abs(span) / (2 * pi))
    step = span / steps

    return [
        Point2(
            center.x + cos(start + step * i) * radius,
            center.y + sin(start + step * i) * radius,
        )
        for i in range(steps + 1)
    ]
