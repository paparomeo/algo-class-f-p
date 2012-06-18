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

    import pdb; pdb.set_trace()

    if len(a) == 1:
        return 100 * (int(a) * int(c)) + 10 * (int(a) * int(d) + int(b) * int(c)) + int(b) * int(d)
    else:
        return 10**n * (mul(a, c)) + 10**(n/2) * (mul(a, d) + mul(b, c)) + mul(b, d)
