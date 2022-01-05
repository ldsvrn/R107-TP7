#!/usr/bin/env python3

import sys
import os
import getopt


def aide(msg):
    print(msg)
    print(...)  # affiche le nom du script et comment il faut appeler ce script
    exit()


    def recherche(dossier, fichier):
        contenuDuRépertoire = os.listdir(...)


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

    dirs = []
    files = []

    for item in rootdir:  # pour chaque élément (elt) du répertoire
        if os.path.isdir(item):  # si c’est un dossier
            dirs.append(os.path.join(rootdir, item))
        elif os.path.isfile(item):  # sinon si c’est un fichier
            files.append(os.path.join(rootdir, item))


if __name__ == '__main__':
    main(sys.argv[1:])
