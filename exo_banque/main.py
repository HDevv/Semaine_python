from csv_utils import CsvManager
from bank import CompteParticulier

# 1️ Test du générateur CSV
print("\n📄 Lecture du fichier CSV ligne par ligne avec `yield`:")
for ligne in CsvManager.lire_csv_en_generateur("data.csv"):
    print(ligne)  # Affiche chaque ligne du CSV une par une

# 2️ Test du générateur d'historique bancaire
compte = CompteParticulier("Dupont", "Jean", 30, "Paris", "123456", 1000)
compte.deposer(500)
compte.retirer(200)

print("\n📜 Historique des transactions (avec `yield`):")
for transaction in compte.historique_transactions():
    print(transaction)  # Affiche transactions une par une
