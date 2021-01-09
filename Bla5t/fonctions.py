#By Ghislain Demael
#Aidé par Maxime Tardieu
import listeCartes as lc
import random
pioche =[]
defausse = []

joueur1, joueur2, joueur3 = [],[],[]
joueurs = [joueur1, joueur2, joueur3] # lorsque l'on utilisera les fonctions on appellera le joueur1 par l'entier 0, joueur2 par 1 ...
def piocher(joueur, nbrcartesapiocher):
    for i in range(0, nbrcartesapiocher) :
        joueurs[joueur].append(lc.Carte(pioche[0].valeur, pioche[0].nom))
        #pioche.append(list(cartes.keys())[random.randint(0,len(cartes))]) #Si besoin d'une pioche illimitée


def voirmain(joueur):
    for i in range(0,len(joueurs[joueur])):
        print(joueurs[joueurs.find(joueur)][0], joueurs[joueurs.find(joueur)][1]) #jsp ce que tu veux print faudra que tu le change


def defausser(carte):
    defausse.insert(0,lc.Carte(carte.valeur, carte.nom))

def voirdefausse():
    for i in range(len(defausse)):
        print(defausse[i].valeur, defausse[i].nom)

def voirhautdefausse():
    print("La carte en haut de la défausse est : ", defausse[0].valeur, defausse[0].nom, "\n")

cartes = {lc.Ezmo : 4,
          lc.Bob : 4,
          lc.Flies: 4,
          lc.Shark: 4,
          lc.Robot: 4,
          lc.Brandon: 2,
          lc.Diana: 2,
          lc.Alien: 4,
          lc.Sprout: 4,
          lc.Yeti: 4,
          lc.Propzilla: 4,
          }

def initpioche() :
    for i in range(0, len(cartes)):
        for j in range(0,list(cartes.values())[i]):
            pioche.append(cartes.keys)
    defausse.append(list(cartes.keys())[random.randint(0, len(cartes))]) #tu demande la défausse alors qu'il y a rien dedans docn c'est un fix temporaire




def piochevide():
    if len(pioche) == 0:
        for i in defausse[1:]:
            pioche.append(lc.Carte(defausse[0].valeur, defausse[0].nom))
            del defausse[0]
        random.shuffle(pioche)


def cartepiochee():
    print("La carte piochée :", pioche[0].valeur, pioche[0].nom)


def voirCarteHautPioche():
    print("La carte en haut de la pioche est : ", pioche[0].valeur, pioche[0].nom)


def choixJoueur():
    choixJoueur = input("D = Defausser une carte, P = Piocher, E = Echanger : ")


def piocherEchanger(Joueur):
    carteEchange = int(input("Avec quelle carte ? 1, 2, 3, 4 : "))
    for j in range(1, 6):
        if carteEchange == j:
            defausser(cartesJ1[j-1])
            cartesJ1[j-1] = lc.Carte(pioche[0].valeur, pioche[0].nom)
            del pioche[0]



def defausser():
    carteAdefausser = input("Quelle carte voulez-vous défausser ? 1, 2 3 4 ou 5 >:( ou 6 >:(( : ")
    for i in range(1, 6):
        if carteAdefausser == str(i):
            if int(cartesJ1[i-1].valeur) == int(defausse[i-1].valeur):
                defausser(cartesJ1[i-1])
                cartesJ1[i-1] = lc.Carte(0, "Vide")
            else:
                print("Perdu, carte de pénalité")
                piocher(1)



def direbla5t():
    condBlast = input("Voulez-vous dire Bla5t ? (oui/OUI ou non/NON) :").lower
    if condBlast == "oui" or condBlast == "o":
        dernierTourJ1 = True
    elif condBlast == "non" or condBlast == "n":
        dernierTourJ1 = True
