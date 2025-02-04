import ipaddress
import fileinput

# ==============================
# 1. Vérifier un dictionnaire d'adresses IP avec try-except
# ==============================

def detecter_version_ip(ip):
    """Détecte IPv4, IPv6 ou invalide avec gestion des erreurs"""
    try:
        if ipaddress.IPv4Address(ip):
            return "IPv4"
    except ipaddress.AddressValueError:
        pass

    try:
        if ipaddress.IPv6Address(ip):
            return "IPv6"
    except ipaddress.AddressValueError:
        pass

    return "Invalide"

# Vérifie un dictionnaire {hôte: adresse IP} avec gestion des erreurs
def verifier_dictionnaire_ip(dico_ip):
   
    resultats = {}
    
    for host, ip in dico_ip.items():
        try:
            type_ip = detecter_version_ip(ip)
            resultats[host] = {"adresse": ip, "type": type_ip}
        except Exception as e:
            resultats[host] = {"adresse": ip, "type": "Erreur", "message": str(e)}

    return resultats

# ==============================
# 2. Remplacement de certaines lettres par 'x' dans un fichier avec fileinput
# ==============================

def remplacer_lettres_fichier(chemin_fichier, lettres_a_remplacer):
    
    try:
        with fileinput.input(chemin_fichier, inplace=True) as fichier:
            for ligne in fichier:
                nouvelle_ligne = ligne
                for lettre in lettres_a_remplacer:
                    nouvelle_ligne = nouvelle_ligne.replace(lettre, "x")
                print(nouvelle_ligne, end="")  # Remplace la ligne dans le fichier

        print("\n✅ Remplacement terminé avec succès !")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{chemin_fichier}' n'existe pas.")
    except PermissionError:
        print(f"❌ Erreur : Permission refusée pour modifier '{chemin_fichier}'.")
    except Exception as e:
        print(f"⚠️ Erreur inattendue : {str(e)}")

# ==============================
# 3. Stocker un fichier dans un dictionnaire
# ==============================

def lire_fichier_dans_dictionnaire(chemin_fichier):
    contenu_dict = {}
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            for numero, ligne in enumerate(fichier, start=1):
                contenu_dict[numero] = ligne.strip()

        return contenu_dict

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{chemin_fichier}' n'existe pas.")
        return {}  # err = Dictionnaire vide au lieu de None

    except Exception as e:
        print(f"⚠️ Erreur inattendue : {str(e)}")
        return {}  # err = Dictionnaire vide en cas d'autre erreur

# ==============================
# 4. Affichage formaté du fichier
# ==============================

def afficher_contenu_fichier(dictionnaire_contenu):
    if not dictionnaire_contenu:
        print("\nFichier vide ou introuvable. Aucun contenu à afficher.")
        return
    
    print("\nContenu du fichier :")
    for ligne_num, texte in dictionnaire_contenu.items():
        nb_caracteres = len(texte)
        print(f"Ligne {ligne_num} : {nb_caracteres} caractères → \"{texte}\"")

# ==============================
# Programme principal
# ==============================

if __name__ == "__main__":
    print("--- Bienvenue dans le vérificateur d'adresses IP et fichiers ! ---")

    # -1️- Vérification d'une adresse IP entrée par l'utilisateur
    user_ip = input("Entrez une adresse IP pour vérifier si elle est valide (x.x.x.x) : ").strip()
    type_ip = detecter_version_ip(user_ip)
    
    if type_ip == "Invalide":
        print(f"❌ Adresse {user_ip} invalide.")
    else:
        print(f"✅ L'adresse {user_ip} est une {type_ip} valide !")

    # -2️- Vérification d'un dictionnaire d'adresses IP
    print("\n Vérification d'un dictionnaire d'adresses IP :")
    dico_exemple = {
        "Serveur 1": "192.168.1.10",
        "Serveur 2": "2001:db8::ff00:42:8329",
        "Routeur": "fe80::1",
        "Machine Inconnue": "999.999.999.999",
        "Erreur Simulée": "NotAnIP"
    }
    resultats_dico = verifier_dictionnaire_ip(dico_exemple)

    for host, data in resultats_dico.items():
        print(f"{host} → {data['adresse']} ({data['type']})")
        if data["type"] == "Erreur":
            print(f"⚠️ Erreur détectée : {data['message']}")

    # -3️- Remplacement de lettres dans le fichier "resultats.txt"
    chemin = "/home/baguette/mon_projet/resultats.txt"
    lettres = ["a", "e", "i", "o", "u"]
    remplacer_lettres_fichier(chemin, lettres)

    # -4️- Lecture et affichage du fichier
    dictionnaire_contenu = lire_fichier_dans_dictionnaire(chemin)

    print("\nContenu du fichier sous forme de dictionnaire :")
    afficher_contenu_fichier(dictionnaire_contenu)

    print("\n✅ Programme terminé ! ")
