#!/usr/bin/python3
for i in range(0, 100):
    print("{:02d}".format(i), end='')
    if i != (100 - 1):
        print(", ", end='')
print("\n")
