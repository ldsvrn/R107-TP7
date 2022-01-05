#!/usr/bin/env python3

import sys
import os


def main(argv):
    if not argv:
        print("ERREUR: Pas assez d'arguments!")
        quit()

    for dir in argv:
        if not os.path.exists(dir):
            print(f"ERREUR: Le dossier {dir} n'existe pas!")
            continue

        # os.chdir(dir)
        files = []
        dirs = []
        for obj in os.listdir(dir):
            if os.path.isdir(dir + "/" + obj):
                dirs.append(obj)
            elif os.path.isfile(dir + "/" + obj):
                files.append(obj)

    print("\t---- DOSSIERS ----")
    for i in dirs:
        print(i, end=" ")

    print("\n\t---- FICHIERS ----")
    for i in files:
        print(i, end=" ")


if __name__ == '__main__':
    main(sys.argv[1:])
