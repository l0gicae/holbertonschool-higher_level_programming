#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c != ord('e') and c != ord('q'):
        print("{}".format(chr(c)), end="")
