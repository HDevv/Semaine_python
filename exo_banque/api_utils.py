import requests

# Gère les requêtes API (GET/POST) et retourne données sous f de dictionnaire
# Gère errs si code 4xx

class ApiManager:
    
    @staticmethod
    def requete_api(url, methode="GET", donnees=None):
        try:
            if methode == "GET":
                response = requests.get(url)
            elif methode == "POST":
                response = requests.post(url, json=donnees)
            else:
                return {"Erreur": "Méthode non supportée"}

            if response.status_code >= 400:
                return {"Erreur": f"Requête échouée avec le code {response.status_code}"}

            return response.json()  

        except requests.RequestException as e:
            return {"Erreur": f"Problème de connexion : {str(e)}"}
