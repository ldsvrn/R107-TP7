#!/usr/bin/env python3
import sys

def main(argv):
    print(len(argv))
    if len(argv) <= 1:
        print("Pas assez d'arguments!")
    else:
        for i in argv:
            print(f"\t=> {i}")


if __name__ == '__main__':
    main(sys.argv[1:])
