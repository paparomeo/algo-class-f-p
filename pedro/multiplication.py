#!/usr/bin/env python3

# FIXME: initial version of times table cheats because it is using a
# multiplication
TIMES_TABLE = { (n, m): n * m for n in range(10) for m in range(10) }


def mult(x, y):
    """
    Implement the multiplication algorithm recursively.
    """
    sx = str(x)
    sy = str(y)
    n = max(len(sx), len(sy))

    if n == 1:  # trivial case
        return TIMES_TABLE[(x, y)]
    else:  # recursive case
        n_2 = n >> 1
        x1, x2 = int(sx[:n_2]), int(sx[n_2:])
        y1, y2 = int(sy[:n_2]), int(sy[n_2:])
        n_2_zeros_str = '0' * n_2
        m1 = int(str(mult(x1, y1)) + n_2_zeros_str + n_2_zeros_str)
        m2 = int(str(mult(x1, y2) + mult(x2, y1)) + n_2_zeros_str)
        m3 = mult(x2, y2)
        return (m1 + m2 + m3)
