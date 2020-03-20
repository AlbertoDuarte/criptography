def modular_exp(b, e, mod):
    if e == 0:
        return 1

    res = modular_exp(b, e//2, mod)
    res = (res * res ) % mod

    if e%2 == 1:
        res = (res * b) % mod

    return res

def gcd(a, b):
    if a == 0:
        return 0, 1, b

    g, x1, y1 = gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return g, x, y
