def afficher_batonnets(n):
    print("Bâtonnets restants :", "|" * n)


def joueur_retrait(n):
    while True:
        try:
            retrait = int(input("Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ? "))
            if retrait in [1, 2, 3] and retrait <= n:
                return retrait
            else:
                print("Choix invalide. Réessayez.")
        except ValueError:
            print("Entrez un nombre valide.")


def maitre_retrait(n):
    return n % 4 if n % 4 != 0 else 1


def jeu_nim():
    print("Épreuve de Logique : Jeu de NIM")
    batonnets = 20
    tour_joueur = True

    while batonnets > 0:
        afficher_batonnets(batonnets)
        if tour_joueur:
            print("C'est votre tour.")
            retrait = joueur_retrait(batonnets)
        else:
            retrait = maitre_retrait(batonnets)
            print(f"Le maître du jeu retire {retrait} bâtonnets.")

        batonnets -= retrait
        if batonnets == 0:
            if tour_joueur:
                print("Vous avez perdu ! Le maître du jeu gagne.")
                return False
            else:
                print("Vous avez gagné ! Félicitations.")
                return True
        tour_joueur = not tour_joueur
