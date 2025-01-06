import random


def introduction():
    print("Bienvenue dans le simulateur Fort Boyard !")
    print("Votre objectif est de réussir 3 épreuves pour gagner des clés.")
    print("Avec ces clés, vous accéderez à la salle du trésor.")
    print("-" * 50)


def composer_equipe():
    equipe = []
    nb_joueurs = int(input("Combien de joueurs dans l'équipe ? (1 à 3) : "))
    while nb_joueurs < 1 or nb_joueurs > 3:
        nb_joueurs = int(input("Erreur. Combien de joueurs voulez-vous inscrire ? (1 à 3) : "))

    for i in range(nb_joueurs):
        print(f"Entrez les informations du joueur {i + 1}:")
        nom = input("Nom : ")
        profession = input("Profession : ")
        leader = input("Est-ce le leader ? (oui/non) : ").strip().lower() == "oui"
        equipe.append({
            "nom": nom,
            "profession": profession,
            "leader": leader,
            "cles_gagnees": 0
        })

    if not any(joueur["leader"] for joueur in equipe):
        print("Aucun leader désigné, le premier joueur sera automatiquement le leader.")
        equipe[0]["leader"] = True

    return equipe


def menu_epreuves():
    print("\nChoisissez une épreuve :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve de Hasard")
    print("4. Énigme du Père Fouras")
    choix = int(input("Votre choix (1-4) : "))
    while choix not in [1, 2, 3, 4]:
        choix = int(input("Choix invalide. Réessayez (1-4) : "))
    return choix


def choisir_joueur(equipe):
    print("\nListe des joueurs :")
    for i, joueur in enumerate(equipe):
        role = "Leader" if joueur["leader"] else "Membre"
        print(f"{i + 1}. {joueur['nom']} ({joueur['profession']}) - {role}")
    choix = int(input("Entrez le numéro du joueur choisi : "))
    while choix < 1 or choix > len(equipe):
        choix = int(input("Numéro invalide. Réessayez : "))
    return equipe[choix - 1]
