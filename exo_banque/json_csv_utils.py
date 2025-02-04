import json
import csv
from pathlib import Path

# Classe pour exporter des dictionnaires en JSON et CSV.
class JsonCsvExporter:
 
    @staticmethod
    def exporter_json(donnees, fichier_json):
        try:
            fichier_json = Path(fichier_json)
            with fichier_json.open("w", encoding="utf-8") as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
            print(f"✅ Données exportées en JSON : {fichier_json}")
        except Exception as e:
            print(f"❌ Erreur lors de l'export JSON : {str(e)}")

    @staticmethod
    def exporter_csv(donnees, fichier_csv, colonnes):
        try:
            fichier_csv = Path(fichier_csv)
            with fichier_csv.open("w", encoding="utf-8", newline="") as f:
                ecrivain = csv.DictWriter(f, fieldnames=colonnes)
                ecrivain.writeheader()
                ecrivain.writerows(donnees)
            print(f"✅ Données exportées en CSV : {fichier_csv}")
        except Exception as e:
            print(f"❌ Erreur lors de l'export CSV : {str(e)}")
