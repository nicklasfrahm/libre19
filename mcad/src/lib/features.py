"""
Shared features that can be reused across several parts.
"""
from os import getenv
from math import ceil, sin, cos, pi
from euclid3 import Point2
from solid import OpenSCADObject
from solid.objects import polygon
from solid.utils import linear_extrude
from .utils import combine


def deg2rad(deg: float):
    """
    Converts degress to radians.
    """
    return pi * (deg / 180)


def arc2d(
    center=Point2(),
    radius=1,
    start=0,
    stop=90,
    segments=512,
):
    """
    Draws an arc of specified `radius` aroung the given `center` point
    from `start` to `end`, where both are angles given in degrees. The
    resolution of the arc can be adjusted via the segments parameter,
    which sets the number of points on a 360 degree full circle.
    """
    resolution = getenv("RESOLUTION")
    if resolution is not None:
        segments = int(resolution)

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


def handle(length=50, width=5) -> OpenSCADObject:
    """
    Create a handle of the specified length and width.
    """
    return combine(
        polygon(
            [
                Point2(0, 0),
                Point2(width, 0),
                *arc2d(Point2(width * 2, -width * 2), width, 180, 270),
                *arc2d(Point2(length - width * 2, -width * 2), width, 270, 360),
                Point2(length - width, 0),
                Point2(length, 0),
                *arc2d(Point2(length - width * 2, -width * 2), width * 2, 360, 270),
                *arc2d(Point2(width * 2, -width * 2), width * 2, 270, 180),
            ],
        ),
        linear_extrude(width),
    )
