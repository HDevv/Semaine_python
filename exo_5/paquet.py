import random
from carte import Carte

# Classe qui génère et gère un paquet de 52 cartes
class PaquetDeCartes:
    
    
    VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    COULEURS = ["Cœur ❤️", "Carreau ♦️", "Trèfle ♣️", "Pique ♠️"]

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for couleur in self.COULEURS for valeur in self.VALEURS]
    
    def melanger(self):
        # Mélange
        random.shuffle(self.paquet)

    def get_cartes(self):
        return self.paquet
