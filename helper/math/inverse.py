from .gcd import gcd

def inverse(a, mod):
    g, x, y = gcd(a, mod)
    return (x + mod) % mod
