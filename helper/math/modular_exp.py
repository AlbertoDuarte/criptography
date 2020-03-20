def modular_exp(b, e, mod):
    if e == 0:
        return 1

    res = modular_exp(b, e//2, mod)
    res = (res * res ) % mod

    if e%2 == 1:
        res = (res * b) % mod

    return res
