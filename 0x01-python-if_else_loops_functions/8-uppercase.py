#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= ord('a')) and (ord(c) <= ord('z')):  # if lowercase
            c = chr(ord(c)-ord('a')+ord('A'))  # subtract 32 to it ascii value
        print("{}".format(c), end='')
    print()
