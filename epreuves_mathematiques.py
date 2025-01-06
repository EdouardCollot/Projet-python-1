import random

def factorielle(n):
    return 1 if n == 0 else n * factorielle(n - 1)

def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print(f"Épreuve de Mathématiques : Calculez la factorielle de {n}.")
    reponse = int(input("Votre réponse : "))
    if reponse == factorielle(n):
        print("Correct ! Vous avez gagné une clé.")
        return True
    else:
        print(f"Incorrect. La bonne réponse était {factorielle(n)}.")
        return False

def epreuve_math():
    return epreuve_math_factorielle()

