"""
Utilities for building the SCAD files and creating objects.
"""
from solid import OpenSCADObject, scad_render_to_file


def build(obj, script, resolution=512):
    """
    Renders an OpenSCAD object to a file in the build directory.
    """
    # Replace file extension of the invoked Python file.
    filename = script.split("/")[-1].replace(".py", ".scad")

    # Render script to output file.
    scad_render_to_file(
        obj,
        f"build/scad/{filename}",
        file_header=f"$fn = {resolution};",
        include_orig_code=False,
    )


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
