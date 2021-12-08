from os import makedirs
from solid import scad_render_to_file


def build(obj, script, resolution=512):
    filename = script.split("/")[-1].replace(".py", ".scad")

    # Create output directory.
    directory = f"build/scad"
    makedirs(directory, exist_ok=True)

    # Render script to output file.
    scad_render_to_file(
        obj,
        f"{directory}/{filename}",
        file_header=f"$fn = {resolution};",
        include_orig_code=False,
    )


def combine(*transforms):
    """Combine an object with the list of transforms."""
    # The first operation must be an OpenSCAD object.
    obj = transforms[0]

    # All other transforms are modification to be applied to the object.
    for transform in transforms[1:]:
        obj = transform(obj)

    return obj
