import random

def bonneteau():
    print("Épreuve de Hasard : Trouvez sous quel bonneteau se cache la clé.")
    essais = 2
    options = ['A', 'B', 'C']
    for _ in range(essais):
        cache = random.choice(options)
        choix = input("Choisissez A, B ou C : ").strip().upper()
        if choix == cache:
            print("Bravo ! Vous avez trouvé la clé.")
            return True
        else:
            print("Incorrect. Essayez encore.")
    print(f"Perdu. La clé était sous {cache}.")
    return False

def lancer_de_des():
    print("Épreuve de Hasard : Lancez deux dés. Le premier à obtenir un 6 gagne.")
    essais = 3
    for _ in range(essais):
        joueur = random.randint(1, 6), random.randint(1, 6)
        maitre = random.randint(1, 6), random.randint(1, 6)
        print(f"Vous : {joueur}, Maître du jeu : {maitre}")
        if 6 in joueur:
            print("Vous gagnez une clé !")
            return True
        if 6 in maitre:
            print("Le maître du jeu gagne. Vous perdez.")
            return False
    print("Aucun gagnant après 3 essais.")
    return False

def epreuve_hasard():
    epreuves = [bonneteau, lancer_de_des]
    return random.choice(epreuves)()
