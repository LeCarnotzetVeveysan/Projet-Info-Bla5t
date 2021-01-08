from fonctions import *
from listeCartes import *

condFinPartie = False

'''Boucle de Partie'''
while not condFinPartie:

    random.shuffle(pioche)

    for i in range(4):
        piocher(1)
        piocher(2)
        piocher(3)

    defausse.append(Carte(pioche[0].valeur, pioche[0].nom))
    del pioche[0]

    voirMain(1)

    voirHautDefausse()

    finManche = False
    dernierTourJ1 = False
    dernierTourJ2 = False
    dernierTourJ3 = False

    '''Boucle de Manche'''
    while not finManche:

        if dernierTourJ1 is True:
            finManche = True
            break

        piocheVide()

        choixJoueur()

        if choixJoueur == "D" or choixJoueur == "d":

            J1Defausser()

        if choixJoueur == "P" or choixJoueur == "p":

            cartePiochee()

            choixPJ1 = input("Voulez-vous l'échanger (E) ou la défausser (D) ? : ")

            if choixPJ1 == "E" or choixPJ1 == "e":
                J1PiocherEchanger()
            elif choixPJ1 == "D" or choixPJ1 == "d":
                defausser(pioche[0])
                '''Actions des différentes cartes'''
                del pioche[0]

        if choixJoueur == "E" or choixJoueur == "e":
            carteAEchanger = input("Quelle carte voulez-vous échanger ? 1, 2, 3, 4, ou 5, 6")
            if carteAEchanger == "1":
                break

        J1DireBla5t()

        voirMain(1)
        voirDefausse()

""
