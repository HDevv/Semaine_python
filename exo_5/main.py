from paquet import PaquetDeCartes
from distribution import Distributeur

# ==============================
# Programme Principal
# ==============================
if __name__ == "__main__":
    print("\n Bienvenue !")

    # Création du paquet et mélange
    paquet = PaquetDeCartes()
    paquet.melanger()

    # Demande du nombre de joueurs
    while True:
        try:
            nb_joueurs = int(input("\n Combien de joueurs ? "))
            if nb_joueurs > 0:
                break
            else:
                print("⚠️ Le nombre de joueurs doit être supérieur à 0.")
        except ValueError:
            print("⚠️ Veuillez entrer un nombre valide.")

    # Distribution des cartes
    distribution, cartes_en_trop = Distributeur.distribuer_cartes(paquet.get_cartes(), nb_joueurs)

    # Affichage des mains des joueurs
    for joueur, cartes in distribution.items():
        print(f"\n {joueur} reçoit : {cartes}")

    # Gestion des cartes restantes
    if cartes_en_trop:
        print(f"\n⚠️ Cartes restantes (non distribuées) : {cartes_en_trop}")

    print("\n✅ Distribution terminée ! Amusez-vous bien !")
