#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    userArgs = argv[1:] # ignoring the filename with idx 0
    size = len(userArgs)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) is not 1 else "argument",
                 "." if (size) is 0 else ":"))
    for idx, arg in enumerate(userArgs):
        print("{:d}: {:s}".format(idx + 1, arg))
