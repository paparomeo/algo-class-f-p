# coding:utf-8

def mul(x, y):
    x = str(x)
    y = str(y)
    n = len(x)

    if len(y) != n:
        print "Numbers must have same number of digits."
        return
    if n % 2:
        print "Numbers must have an even number of digits."
        return
    
    # Calculate parts
    a = x[:n / 2]
    b = x[n / 2:]
    c = y[:n / 2]
    d = y[n / 2:]

    if len(a) == 1:
        ac = int(a) * int(c)
        ad = int(a) * int(d)
        bc = int(b) * int(c)
        bd = int(b) * int(d)
        return int('%d00' % ac) + int('%d0' % (ad + bc)) + bd
    else:
        factor1 = 10**n
        factor2 = 10**(n/2)
        return int('%d%d' % (mul(a, c), factor1)) + int('%d%d' % (mul(a, d) + mul(b, c), factor2)) + mul(b, d)
