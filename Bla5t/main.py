import fonctions as fc
import random
condFinPartie = False

while not condFinPartie: #Boucle de Partie
    random.shuffle(fc.pioche)
    fc.initpioche()
    fc.voirmain(0)
    fc.voirhautdefausse()
    finManche = False
    dernierTourJ1 = False
    dernierTourJ2 = False
    dernierTourJ3 = False
    while not finManche: #boucle de manche
        if dernierTourJ1 is True:
            finManche = True
            break
        fc.piochevide()
        fc.choixJoueur()
        if fc.choixJoueur == "D" or fc.choixJoueur == "d":
            fc.defausser(1)
        if fc.choixJoueur == "P" or fc.choixJoueur == "p":
            fc.cartePiochee()
            choixPJ1 = input("Voulez-vous l'échanger (E) ou la défausser (D) ? : ").lower
            if choixPJ1 == "e":
                fc.J1PiocherEchanger()
            elif choixPJ1 == "d":
                fc.defausser(fc.pioche[0])#Actions des différentes cartes

                del fc.pioche[0]
        if  fc.choixJoueur == "e":
            carteAEchanger = input("Quelle carte voulez-vous échanger ? 1, 2, 3, 4, ou 5, 6")
            if carteAEchanger == "1":
                break
        fc.direbla5t()
        fc.voirMain(1)
        fc.voirdefausse()