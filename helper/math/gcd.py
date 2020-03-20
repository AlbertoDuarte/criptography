def gcd(a, b):
    if a == 0:
        return 0, 1, b

    g, x1, y1 = gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return g, x, y
