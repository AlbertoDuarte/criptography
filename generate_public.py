import json
from helper.math.modular_exp import modular_exp

with open('info.json', 'r') as f:
    data = json.load(f)
    p = data["prime"]
    gen = data["generator"]

try:
    key = int(input("Insert your private key: "))

    assert(int(gen) < int(p))
except ValueError:
    print("All input should be positive integers and g < p")

public = modular_exp(int(gen), int(key), int(p))
print("Your public key is:")
print(public)
