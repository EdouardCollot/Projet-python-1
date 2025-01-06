import json
import random

def charger_enigmes(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erreur : le fichier {fichier} est introuvable.")
        return []
    except json.JSONDecodeError:
        print(f"Erreur : le fichier {fichier} n'est pas correctement formaté.")
        return []

def enigme_pere_fouras():
    enigmes = charger_enigmes('data/enigmesPF.json')
    if not enigmes:
        print("Impossible de jouer cette épreuve. Aucun fichier d'énigmes chargé.")
        return False
    enigme = random.choice(enigmes)
    print("\nÉpreuve du Père Fouras : Résolvez cette énigme pour obtenir une clé !")
    print("Énigme :", enigme["question"])
    essais = 3
    while essais > 0:
        reponse = input("Votre réponse : ").strip().lower()
        if reponse == enigme["reponse"].lower():
            print("Correct ! Vous avez gagné une clé.")
            return True
        essais -= 1
        if essais > 0:
            print(f"Incorrect. Il vous reste {essais} essai(s).")
        else:
            print(f"Perdu ! La réponse correcte était : {enigme['reponse']}.")
    return False
