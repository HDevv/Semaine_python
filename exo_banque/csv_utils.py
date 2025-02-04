import csv
from pathlib import Path


    # Classe pour gérer les fichiers CSV (lecture et modification)
    
class CsvManager:
    
    @staticmethod
    def lire_csv_en_generateur(fichier_source):
        
        fichier_source = Path(fichier_source)

        try:
            with fichier_source.open("r", encoding="utf-8") as csv_source:
                lecteur = csv.reader(csv_source)
                for ligne in lecteur:  # Utilisation de yield
                    yield ligne  # Retourne ligne une par une
        except FileNotFoundError:
            print(f"❌ Erreur : Le fichier {fichier_source} n'existe pas.")
