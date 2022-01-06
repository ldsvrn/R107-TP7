#!/usr/bin/env python3

import sys
import os
import getopt

# HAHAHAHAH CA FONCTIONNE SANS OS.WALK :!!!!!!!!!!!!!!!!!!!!!


def help(error, errno = 132):
    print(f"ERREUR: {error}")
    print("\t# Script de recherche:")
    print("Utilisation: ./find.py -d DOSSIER -f FICHIER A CHERCHER")
    quit(errno)


results = []
dirs = []


def findFile(dir, toFind):
    for obj in os.listdir(dir):
        path = os.path.join(dir, obj)
        if os.path.isdir(path):
            dirs.append(path)
        elif os.path.isfile(path):
            if obj == toFind:
                results.append(path)


def main(argv):
    if not argv:
        help("Pas assez d'arguments!", 22)

    try:
        opts, args = getopt.getopt(argv, "d:f:")
    except:
        help("arguments!")

    rootdir = ""
    toFind = ""
    for i in opts:
        match i[0]:
            case '-d':
                rootdir = i[1]
            case '-f':
                toFind = i[1]

    if not os.path.exists(rootdir):
        print(f"ERREUR: {rootdir} n'existe pas!")
        quit(2)
    elif not os.path.isdir(rootdir):
        print(f"ERREUR: {rootdir} n'est pas un dossier!")
        quit(20)

    dirs.append(rootdir)
    for item in dirs:
        # print(f"for i in dirs: i {item} => dirs = {dirs}")
        findFile(item, toFind)

    for i in results:
        print(i)


if __name__ == '__main__':
    main(sys.argv[1:])
    quit(0)
