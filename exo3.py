import requests
import csv
import json
from pathlib import Path

# ==============================
# 1. Exécuter une req API (GET/POST) et récupérer les données en dictionnaire
# ==============================
# Ici on utilisera JSONPlaceholder qui est une API factice ne nécéssitant pas de création de compte 

def requete_api(url, methode="GET", donnees=None):
    try:
        if methode == "GET":
            response = requests.get(url)
        elif methode == "POST":
            response = requests.post(url, json=donnees)
        else:
            return {"Erreur": "Méthode non supportée"}
        # Gère les erreurs si code 4xx.
        if response.status_code >= 400: 
            return {"Erreur": f"Requête échouée avec le code {response.status_code}"}
        
        return response.json() 

    except requests.RequestException as e:
        return {"Erreur": f"Problème de connexion : {str(e)}"}

# ==============================
# 2. Importer un CSV, modifier son contenu et sauvegarder dans un autre CSV
# ==============================

def modifier_csv(fichier_source, fichier_destination):
    try:
        with fichier_source.open("r", encoding="utf-8") as csv_source:
            lecteur = csv.reader(csv_source)
            donnees = [ligne for ligne in lecteur]

        # Ajouter "MODIFIÉ" à la fin de chaque ligne
        for ligne in donnees:
            ligne.append("MODIFIÉ")

        with fichier_destination.open("w", encoding="utf-8", newline="") as csv_dest:
            ecrivain = csv.writer(csv_dest)
            ecrivain.writerows(donnees)

        print(f"✅ Fichier modifié et sauvegardé dans : {fichier_destination}")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier {fichier_source} n'existe pas.")

# ==============================
# 3. Exporter un dictionnaire vers un fichier JSON
# ==============================

def exporter_json(donnees, fichier_json):
    try:
        with fichier_json.open("w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        print(f"✅ Données exportées en JSON : {fichier_json}")
    except Exception as e:
        print(f"❌ Erreur lors de l'export JSON : {str(e)}")

# ==============================
# 4. Exporter un dictionnaire vers un fichier CSV
# ==============================

def exporter_csv(donnees, fichier_csv, colonnes):
    try:
        with fichier_csv.open("w", encoding="utf-8", newline="") as f:
            ecrivain = csv.DictWriter(f, fieldnames=colonnes)
            ecrivain.writeheader()
            ecrivain.writerows(donnees)

        print(f"✅ Données exportées en CSV : {fichier_csv}")

    except Exception as e:
        print(f"❌ Erreur lors de l'export CSV : {str(e)}")

# ==============================
# Programme principal
# ==============================

if __name__ == "__main__":
    print("--- Début du programme ---")

    # Définition du dossier de travail avec Pathlib
    dossier_projet = Path("/home/baguette/mon_projet") 

    # 1️ Test API avec une requête GET
    url_api = "https://jsonplaceholder.typicode.com/posts/1"  
    resultat_api = requete_api(url_api, "GET")
    print("📥 Données API récupérées :", resultat_api)

    # 2️ Test modification CSV
    fichier_csv_source = dossier_projet / "data.csv"  # Fichier CSV original
    fichier_csv_modifie = dossier_projet / "data_modifie.csv"  # Nv fichier CSV modifié
    modifier_csv(fichier_csv_source, fichier_csv_modifie)

    # 3️ Test export JSON
    fichier_json = dossier_projet / "donnees.json"
    exporter_json(resultat_api, fichier_json)

    # 4️ Test export CSV
    fichier_csv_export = dossier_projet / "donnees_export.csv"
    colonnes = ["userId", "id", "title", "body"]  
    if isinstance(resultat_api, dict):  # Convertir en liste de dicos pour CSV
        resultat_api = [resultat_api]
    exporter_csv(resultat_api, fichier_csv_export, colonnes)

    print("✅ Programme terminé !")
