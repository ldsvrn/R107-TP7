#!/usr/bin/env python3

import sys
import os
import getopt


def help(error, errno = 132):
    print(f"ERREUR: {error}")
    print("\t# Script de recherche:")
    print("Utilisation: ./find.py -d DOSSIER -f FICHIER A CHERCHER")
    quit(errno)


def main(argv):
    if not argv:
        help("Pas assez d'arguments!", 22)

    try:
        opts, args = getopt.getopt(argv, "d:f:")
    except:
        help("arguments!")

    rootdir = ""
    toSearch = ""
    for i in opts:
        match i[0]:
            case '-d':
                rootdir = i[1]
            case '-f':
                toSearch = i[1]

    if not os.path.exists(rootdir):
        print(f"ERREUR: {rootdir} n'existe pas!")
        quit(2)
    elif not os.path.isdir(rootdir):
        print(f"ERREUR: {rootdir} n'est pas un dossier!")
        quit(20)

    results = []
    for (root, dirs, files) in os.walk(rootdir):
        if toSearch in files:
            results.append(os.path.join(root, toSearch))

    for i in results:
        print(i)


if __name__ == '__main__':
    main(sys.argv[1:])
    quit(0)
