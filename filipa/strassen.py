# encoding:utf-8

def seven_products(a, b, c, d, e, f, g, h):
    """
    Returns the seven products of Strassen's algorithm
    """
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    return p1, p2, p3, p4, p5, p6, p7

def multiply_matrices(m1, m2):
    pass
