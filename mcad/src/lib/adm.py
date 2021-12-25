"""
A library containing utilities for additive manufacturing.
"""


def dimension(dim: float, tol: int = 0, step: float = 0.4) -> float:
    """
    Given a dimension, this function will round down to the
    next multiple of the dimension. An additional parameter
    `tol` can be specified to add `tol` additional steps to
    add a tolerance to accommodate for shrinking.
    """
    # Add small value to reduce risk of the remainder being zero.
    dim += 1e-10
    return (dim // step) * step + tol * step
