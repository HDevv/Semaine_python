# Distribution des cartes aux joueurs
class Distributeur:
   
    @staticmethod
    def distribuer_cartes(paquet, nb_joueurs):
        
        # Distribue équitablement les cartes aux joueurs
        # Si les cartes ne peuvent pas être partagées également, on met celles qui restent de côté 
        
        if nb_joueurs < 1:
            raise ValueError("Il doit y avoir au moins un joueur !")
        
        cartes_par_joueur = len(paquet) // nb_joueurs
        cartes_restantes = len(paquet) % nb_joueurs

        distribution = {f"Joueur {i+1}": paquet[i * cartes_par_joueur:(i+1) * cartes_par_joueur] 
                        for i in range(nb_joueurs)}

        cartes_en_trop = paquet[-cartes_restantes:] if cartes_restantes > 0 else []

        return distribution, cartes_en_trop
