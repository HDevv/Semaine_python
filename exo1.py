import ipaddress  # Module Python pour gérer les adresses IP

def est_ipv4_valide(ip):
    """Vérifie si adresse = IPv4 valide"""
    try:
        ipaddress.IPv4Address(ip)  # Tente de créer une adresse IPv4
        return True  # Si l'adresse est correcte
    except ipaddress.AddressValueError:
        return False  # Sinon, l'adresse est invalide

def est_ipv6_valide(ip):
    """Vérifie si adresse = IPv6 valide"""
    try:
        ipaddress.IPv6Address(ip)  # Tente de créer une adresse IPv6
        return True
    except ipaddress.AddressValueError:
        return False
    
# Détecte si adresse = IPv4, IPv6 ou invalide
def detecter_version_ip(ip):
    
    if est_ipv4_valide(ip):
        return "IPv4"
    elif est_ipv6_valide(ip):
        return "IPv6"
    else:
        return "Invalide"
    

# Vérifie une liste d'adresses IP et retourne un dictionnaire {adresse: type}
def verifier_liste_ip(liste_ip):
    
    resultats = {}
    for ip in liste_ip:
        resultats[ip] = detecter_version_ip(ip)  # Associe chaque IP à son type
    return resultats

# Vérifie un dictionnaire {hôte: adresse IP} et retourne résultats
def verifier_dictionnaire_ip(dico_ip):

    resultats = {}
    for host, ip in dico_ip.items():
        resultats[host] = {
            "adresse": ip,
            "type": detecter_version_ip(ip)
        }
    return resultats

# =======================
# Programme principal
# =======================
if __name__ == "__main__":
    print("Bienvenue dans le vérificateur d'adresses IP !")
    
    # Demande une adresse IP à l'utilisateur
    user_ip = input("Entrez une adresse IP pour vérifier si elle est valide : ").strip()
    type_ip = detecter_version_ip(user_ip)
    
    if type_ip == "Invalide":
        print(f"❌ Adresse {user_ip} invalide.")
    else:
        print(f"✅ Adresse {user_ip} est une {type_ip} valide !")

    # Vérification d'une liste d'adresses IP
    print("\n Vérification d'une liste d'adresses IP :")
    liste_exemple = ["192.168.1.1", "2001:db8::ff00:42:8329", "300.300.300.300", "fe80::1"]
    resultats_liste = verifier_liste_ip(liste_exemple)

    for ip, type_ip in resultats_liste.items():
        if type_ip == "Invalide":
            print(f"❌ {ip} → Adresse invalide")
        else:
            print(f"✅ {ip} → {type_ip}")

    # Vérification d'un dictionnaire avec des hosts
    print("\n Vérification d'un dictionnaire d'adresses IP :")
    dico_exemple = {
        "Serveur 1": "192.168.1.10",
        "Serveur 2": "2001:db8::ff00:42:8329",
        "Routeur": "fe80::1",
        "Machine Inconnue": "999.999.999.999"
    }
    resultats_dico = verifier_dictionnaire_ip(dico_exemple)

    for host, data in resultats_dico.items():
        if data["type"] == "Invalide":
            print(f"❌ {host} → {data['adresse']} (Adresse invalide)")
        else:
            print(f"✅ {host} → {data['adresse']} ({data['type']})")

    print("\n✅ Programme terminé !")
