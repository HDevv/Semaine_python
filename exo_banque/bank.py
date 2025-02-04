# Identité du client 
class IdentiteClient:
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    def afficher_info(self):
        return f"Client: {self.nom} {self.prenom}, {self.age} ans, Adresse: {self.adresse}"

# Gestion du compte bancaire 
class CompteBancaire:

    def __init__(self, numero_compte, solde=0):
        self.numero_compte = numero_compte
        self.solde = solde
        self._transactions = []  

    def deposer(self, montant):
        self.solde += montant
        self._transactions.append(f"Dépôt de {montant}€")
        print(f"✅ Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€")

    def retirer(self, montant):
        if montant > self.solde:
            print("❌ Fonds insuffisants.")
        else:
            self.solde -= montant
            self._transactions.append(f"Retrait de {montant}€")
            print(f"✅ Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")

    def afficher_solde(self):
        return f"Compte {self.numero_compte} - Solde : {self.solde}€"

    def historique_transactions(self):
        for transaction in self._transactions:
            yield transaction  # Utilisation de yield pour économiser de la mémoire


# Classe enfant qui hérite des deux précédentes 
class CompteParticulier(CompteBancaire, IdentiteClient):
    def __init__(self, nom, prenom, age, adresse, numero_compte, solde=0):
        IdentiteClient.__init__(self, nom, prenom, age, adresse)
        CompteBancaire.__init__(self, numero_compte, solde)

    def afficher_details(self):
        return f"{self.afficher_info()} | {self.afficher_solde()}"
