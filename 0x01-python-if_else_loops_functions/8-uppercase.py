#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        Vee = ord(c)
        if Vee >= 97 and Vee <= 122:
            result += chr(Vee - 32)
        else:
            result += c
    print("{}".format(result))
