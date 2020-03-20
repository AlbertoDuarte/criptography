def num2text(num):
    to_letter = {99: ' ', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h',
                 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p',
                 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}

    string = str(num)
    # assert(len(string) % 2 == 0)

    res = ""
    i = 0
    while i < len(string):
        pair = int(string[i] + string[i+1])
        res = res + to_letter[pair]
        i += 2

    return res
