#!/usr/bin/env python3

import sys
import os


def main(argv):
    if not argv:
        print("ERREUR: Pas assez d'arguments!")
        quit()

    for folder in argv:
        if not os.path.exists(folder):
            print(f"ERREUR: Le dossier {folder} n'existe pas!")
            continue

        print(f"\n\t{folder}:")
        for files in os.listdir(folder):
            print(files)


if __name__ == '__main__':
    main(sys.argv[1:])
