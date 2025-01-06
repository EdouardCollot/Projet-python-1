import json
import os
import random

def charger_indices(fichier):
    try:
        if not os.path.exists(fichier):
            print(f"Erreur : Le fichier '{fichier}' est introuvable.")
            return {}

        with open(fichier, 'r', encoding='utf-8') as f:
            indices = json.load(f)
        return indices
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier '{fichier}' n'est pas correctement formaté.")
        return {}
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
        return {}

def salle_de_tresor():
    chemin_fichier = os.path.join('data', 'indicesSalle.json')
    data = charger_indices(chemin_fichier)

    if not data:
        print("Impossible de jouer l'épreuve finale. Aucun fichier d'indices valide.")
        return False
    annee = random.choice(list(data.keys()))
    emission = random.choice(data[annee])
    indices = emission["indices"]
    mot_code = emission["mot_code"]

    print("\n--- Salle du Trésor ---")
    print("Vous devez deviner le mot-code à partir des indices suivants :")
    for i, indice in enumerate(indices):
        print(f"{i + 1}. {indice}")
    essais = 3
    while essais > 0:
        reponse = input("Quel est le mot-code ? ").strip().lower()
        if reponse == mot_code.lower():
            print("Bravo ! Vous avez débloqué la salle du trésor.")
            return True
        essais -= 1
        if essais > 0:
            print(f"Incorrect. Il vous reste {essais} essai(s).")
        else:
            print(f"Perdu ! Le mot-code était : {mot_code}.")
    return False
