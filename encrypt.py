from helper.math.modular_exp import modular_exp
from helper.text.text2num import text2num

with open("info.json", "r") as f:
    data = json.load(f)
    p = data["prime"]

exp = int(input("Insert your private key: "))
numb = int(input("Insert third party public key: "))
key = modular_exp(numb, exp, p)

print(key)

msg_string = str(input("Insert the message to be encrypted: "))

num = text2num(msg_string)

print(num)

res = (key * num) % p
print(str(res))
