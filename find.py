#!/usr/bin/env python3

import sys
import os
import getopt


def main(argv):
    if not argv:
        print("ERREUR: Pas assez d'arguments!")
        quit(22)

    try:
        opts, args = getopt.getopt(argv, "d:f:")
    except:
        print("Error")
        quit()

    print(opts, args)


if __name__ == '__main__':
    main(sys.argv[1:])
