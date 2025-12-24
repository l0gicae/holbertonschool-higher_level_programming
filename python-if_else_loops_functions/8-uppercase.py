#!/usr/bin/python3
def uppercase(str):
    for c in str:
        o = ord(c)
        if ord('a') <= o <= ord('z'):
            o -= 32
        print("{}".format(chr(o)), end="")
    print()
