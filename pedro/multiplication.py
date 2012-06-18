#!/usr/bin/env python3

# FIXME: initial version of times table cheats because it is using a
# multiplication
TIMES_TABLE = { (str(n), str(m)): str(n * m)
                for n in range(10) for m in range(10) }


def multiplication(x, y):
    """
    Implement the multiplication algorithm recursively.
    """
    digits = max(len(x), len(y))

    if digits == 1:  # trivial case
        return TIMES_TABLE[(x, y)]
    else:
        raise ValueError('input values with more than one digit unsupported!')
