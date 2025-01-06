from fonctions_utiles import introduction, composer_equipe, menu_epreuves, choisir_joueur
from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import jeu_nim
from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_de_tresor


def jeu():
    introduction()
    equipe = composer_equipe()
    cles = 0
    while cles < 3:
        choix = menu_epreuves()
        joueur = choisir_joueur(equipe)
        if choix == 1:
            print("\n--- Épreuve de Mathématiques ---")
            gagne = epreuve_math()
        elif choix == 2:
            print("\n--- Épreuve de Logique ---")
            gagne = jeu_nim()
        elif choix == 3:
            print("\n--- Épreuve de Hasard ---")
            gagne = epreuve_hasard()
        elif choix == 4:
            print("\n--- Énigme du Père Fouras ---")
            gagne = enigme_pere_fouras()
        else:
            print("Choix invalide. Réessayez.")
            continue
        if gagne:
            joueur["cles_gagnees"] += 1
            cles += 1
            print(f"Félicitations, {joueur['nom']} a gagné une clé !")
        print(f"Clés collectées : {cles}/3")
    print("\n--- Salle du Trésor ---")
    if salle_de_tresor():
        print("Félicitations ! Vous avez débloqué la salle du trésor et remporté le jeu.")
    else:
        print("Dommage ! Vous avez échoué à la dernière épreuve.")


if __name__ == "__main__":
    try:
        jeu()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
