import json
from helper.math.modular_exp import modular_exp
from helper.math.inverse import inverse
from helper.text.num2text import num2text

with open("info.json", "r") as f:
    data = json.load(f)
    p = data["prime"]

exp = int(input("Insert your private key: "))
numb = int(input("Insert third party public key: "))
key = modular_exp(numb, exp, p)
inv = inverse(key, p)

assert((key*inv)%p == 1)

msg = 0
msg_string = str(input("Insert the message to be dencrypted: "))
try:
    msg = int(msg_string)
except ValueError:
    print("Error! Message should be only numbers!")

res = (msg*inv) % p
res_string = num2text(res)
print(res_string)
