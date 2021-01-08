from listeCartes import *
import random


def piocher(joueur):
    if joueur == 1:
        cartesJ1.append(Carte(pioche[0].valeur, pioche[0].nom))
    elif joueur == 2:
        cartesJ2.append(Carte(pioche[0].valeur, pioche[0].nom))
    elif joueur == 3:
        cartesJ3.append(Carte(pioche[0].valeur, pioche[0].nom))
    del pioche[0]


def voirMain(joueur):
    if joueur == 1:
        print("Main J1:", "\n", cartesJ1[0].valeur, cartesJ1[0].nom, cartesJ1[1].valeur, cartesJ1[1].nom,
              "\n", cartesJ1[2].valeur, cartesJ1[2].nom, cartesJ1[3].valeur, cartesJ1[3].nom, "\n")
    if joueur == 2:
        print("Main J2:", "\n", cartesJ2[0].valeur, cartesJ2[0].nom, cartesJ2[1].valeur, cartesJ2[1].nom,
              "\n", cartesJ2[2].valeur, cartesJ2[2].nom, cartesJ2[3].valeur, cartesJ2[3].nom, "\n")
    if joueur == 3:
        print("Main J3:", "\n", cartesJ3[0].valeur, cartesJ3[0].nom, cartesJ3[1].valeur, cartesJ3[1].nom,
              "\n", cartesJ3[2].valeur, cartesJ3[2].nom, cartesJ3[3].valeur, cartesJ3[3].nom, "\n")


def defausser(carte):
    defausse.insert(0,Carte(carte.valeur, carte.nom))


def voirDefausse():
    for i in range(len(defausse)):
        print(defausse[i].valeur, defausse[i].nom)


def voirHautDefausse():
    print("La carte en haut de la défausse est : ", defausse[0]. valeur, defausse[0].nom, "\n")


pioche = [Ezmo1, Ezmo2, Ezmo3, Ezmo4, Bob1, Bob2, Bob3, Bob4, Flies1, Flies2, Flies3, Flies4,
          Shark1, Shark2, Shark3, Shark4, Robot1, Robot2, Robot3, Robot4, Brandon1, Brandon2, Diana1, Diana2,
          Creature1, Creature2, Creature3, Creature4, Nutzian1, Nutzian2, Nutzian3, Nutzian4,
          Alien1, Alien2, Alien3, Alien4, Sprout1, Sprout2, Sprout3, Sprout4, Yeti1, Yeti2, Yeti3, Yeti4,
          Propzilla1, Propzilla2, Propzilla3, Propzilla4]

defausse = []

cartesJ1 = []
cartesJ2 = []
cartesJ3 = []


def piocheVide():
    if len(pioche) == 0:
        for i in defausse[1:]:
            pioche.append(Carte(defausse[0].valeur, defausse[0].nom))
            del defausse[0]
        random.shuffle(pioche)


def cartePiochee():
    print("La carte piochée :", pioche[0].valeur, pioche[0].nom)


def voirCarteHautPioche():
    print("La carte en haut de la pioche est : ", pioche[0].valeur, pioche[0].nom)


def choixJoueur():
    choixJoueur = input("D = Defausser une carte, P = Piocher, E = Echanger : ")


def J1PiocherEchanger():
    carteEchange = input("Avec quelle carte ? 1, 2, 3, 4 : ")
    if carteEchange == "1":
        defausser(cartesJ1[0])
        cartesJ1[0] = Carte(pioche[0].valeur, pioche[0].nom)
        del pioche[0]
    elif carteEchange == "2":
        defausser(cartesJ1[1])
        cartesJ1[1] = Carte(pioche[0].valeur, pioche[0].nom)
        del pioche[0]
    elif carteEchange == "3":
        defausser(cartesJ1[2])
        cartesJ1[2] = Carte(pioche[0].valeur, pioche[0].nom)
        del pioche[0]
    elif carteEchange == "4":
        defausser(cartesJ1[3])
        cartesJ1[3] = Carte(pioche[0].valeur, pioche[0].nom)
        del pioche[0]
    elif carteEchange == "5":
        defausser(cartesJ1[3])
        cartesJ1[4] = Carte(pioche[0].valeur, pioche[0].nom)
        del pioche[0]
    elif carteEchange == "6":
        defausser(cartesJ1[3])
        cartesJ1[5] = Carte(pioche[0].valeur, pioche[0].nom)
        del pioche[0]


def J1Defausser():
    carteAdefausser = input("Quelle carte voulez-vous défausser ? 1, 2 3 4 ou 5 >:( ou 6 >:(( : ")
    if carteAdefausser == "1":
        if int(cartesJ1[0].valeur) == int(defausse[0].valeur):
            defausser(cartesJ1[0])
            cartesJ1[0] = Carte(0, "Vide")
        else:
            print("Perdu, carte de pénalité")
            piocher(1)
    elif carteAdefausser == "2":
        if int(cartesJ1[1].valeur) == int(defausse[0].valeur):
            defausser(cartesJ1[1])
            cartesJ1[1] = Carte(0, "Vide")
        else:
            print("Perdu, carte de pénalité")
            piocher(1)
    elif carteAdefausser == "3":
        if int(cartesJ1[2].valeur) == int(defausse[0].valeur):
            defausser(cartesJ1[2])
            cartesJ1[2] = Carte(0, "Vide")
        else:
            print("Perdu, carte de pénalité")
            piocher(1)
    elif carteAdefausser == "4":
        if int(cartesJ1[3].valeur) == int(defausse[0].valeur):
            defausser(cartesJ1[3])
            cartesJ1[3] = Carte(0, "Vide")
        else:
            print("Perdu, carte de pénalité")
            piocher(1)
    elif carteAdefausser == "5":
        if int(cartesJ1[4].valeur) == int(defausse[0].valeur):
            defausser(cartesJ1[4])
            cartesJ1[4] = Carte(0, "Vide")
        else:
            print("Perdu, carte de pénalité")
            piocher(1)
    elif carteAdefausser == "6":
        if int(cartesJ1[5].valeur) == int(defausse[0].valeur):
            defausser(cartesJ1[5])
            cartesJ1[5] = Carte(0, "Vide")
        else:
            print("Perdu, carte de pénalité")
            piocher(1)

def J1DireBla5t():
    condBlast = input("Voulez-vous dire Bla5t ? (oui/OUI ou non/NON) :")
    if condBlast == "oui" or condBlast == "OUI":
        '''Retourner les cartes'''
        dernierTourJ1 = True
