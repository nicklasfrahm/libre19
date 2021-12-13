"""
Shared features that can be reused across several parts.
"""
from euclid3 import Point2
from solid import OpenSCADObject
from solid.objects import polygon
from solid.utils import linear_extrude
from .utils import combine
from .sketch import arc2d


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
