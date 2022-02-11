"""
Utilities for building the SCAD files and creating objects.
"""
from os import getenv
from pathlib import Path
from solid import OpenSCADObject, scad_render_to_file, import_


def build(obj, script, segments=32):
    """
    Renders an OpenSCAD object to a file in the build directory.
    """
    # Fetch output resolution.
    resolution = getenv("RESOLUTION")
    if resolution is not None:
        segments = int(resolution)

    # Replace file extension of the invoked Python file.
    filename = script.split("/")[-1].replace(".py", ".scad")

    # Render script to output file.
    scad_render_to_file(
        obj,
        f"build/scad/{filename}",
        file_header=f"$fn = {segments};",
        include_orig_code=False,
    )


def stl(path: str, convexity: int = 4) -> OpenSCADObject:
    """
    Load an STL file into an OpenSCAD object.
    """
    return import_(str(Path(path).resolve()), convexity=convexity)


def combine(*transforms: OpenSCADObject):
    """
    Combine an object with the list of transforms.
    """
    # The first operation must be an OpenSCAD object.
    obj = transforms[0]

    # All other transforms are modification to be applied to the object.
    for transform in transforms[1:]:
        obj = transform(obj)

    return obj
