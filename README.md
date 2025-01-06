# Projet-python-1

---

## Étapes du développement

### **1. Analyse et planification**
- **Objectif :** Concevoir un simulateur interactif avec des épreuves variées, la gestion d’une équipe, et une conclusion via une salle du trésor.
- **Actions :**
  - Définir les modules nécessaires pour chaque fonctionnalité.
  - Planifier une structure claire et modulaire pour le projet.
  - Identifier les données nécessaires (énigmes, indices, etc.) à stocker dans des fichiers JSON.

---

### **2. Mise en place de la structure**
- **Objectif :** Créer une structure de fichiers cohérente pour organiser le code.
- **Actions :**
  - Création des fichiers principaux : 
    ```
    .
    ├── main.py
    ├── fonctions_utiles.py
    ├── epreuves_mathematiques.py
    ├── epreuves_logiques.py
    ├── epreuves_hasard.py
    ├── enigme_pere_fouras.py
    ├── epreuve_finale.py
    └── data
        ├── enigmesPF.json
        └── indicesSalle.json
    ```
  - Mise en place du squelette des fonctions avec des commentaires explicatifs.

- **Difficultés rencontrées :**
  - Gestion des chemins relatifs pour accéder aux fichiers JSON lors de l'exécution depuis différents environnements.
  - **Solution :** Utilisation de `os.path.join` pour construire dynamiquement les chemins.

---

### **3. Développement des modules**
Chaque module a été implémenté séparément avec des tests pour garantir son bon fonctionnement.

#### **3.1. Fonctions utilitaires (`fonctions_utiles.py`)**
- **Objectif :** Gérer les fonctions génériques (introduction, composition de l'équipe, menu des épreuves).
- **Difficultés :**
  - Validation des saisies utilisateur pour éviter les erreurs (valeurs non numériques, choix hors limites).
  - **Solution :** Boucles de validation et gestion des erreurs avec `try...except`.

#### **3.2. Épreuves mathématiques (`epreuves_mathematiques.py`)**
- **Objectif :** Proposer des calculs (exemple : calcul de la factorielle).
- **Difficultés :**
  - Aucun problème majeur, mais ajout de validations claires pour les saisies.

#### **3.3. Épreuves logiques (`epreuves_logiques.py`)**
- **Objectif :** Implémenter le jeu de Nim.
- **Difficultés :**
  - Comprendre et implémenter la stratégie optimale du maître du jeu.
  - **Solution :** Utilisation du reste modulo 4 pour garantir une stratégie gagnante.

#### **3.4. Épreuves de hasard (`epreuves_hasard.py`)**
- **Objectif :** Proposer des épreuves basées sur le hasard (exemple : bonneteau, lancer de dés).
- **Difficultés :**
  - S'assurer que l'épreuve soit équilibrée pour éviter qu'elle ne devienne frustrante pour le joueur.
  - **Solution :** Limiter les essais et offrir une probabilité raisonnable de réussite.

#### **3.5. Énigmes du Père Fouras (`enigme_pere_fouras.py`)**
- **Objectif :** Charger des énigmes depuis un fichier JSON et poser des questions au joueur.
- **Difficultés :**
  - Gestion des erreurs en cas de fichier JSON manquant ou mal formaté.
  - **Solution :** Vérifications robustes avec `os.path.exists` et `json.JSONDecodeError`.

#### **3.6. Épreuve finale (`epreuve_finale.py`)**
- **Objectif :** Mettre en place une salle du trésor où les joueurs doivent deviner un mot-code.
- **Difficultés :**
  - Gestion dynamique des indices par année et sélection aléatoire.
  - **Solution :** Organisation des données en JSON et utilisation de `random.choice`.

---

### **4. Création des fichiers JSON**
- **Fichiers créés :**
  - **`enigmesPF.json` :** Stocke les énigmes du Père Fouras.
  - **`indicesSalle.json` :** Stocke les indices et mots-codes pour l’épreuve finale.
- **Difficultés :**
  - Une petite erreur de formatage (comme une virgule manquante) rendait le fichier inutilisable.
  - **Solution :** Validation avec des outils comme [JSONLint](https://jsonlint.com/).

---

### **5. Tests et ajustements**
- **Tests effectués :**
  - Scénarios complets pour chaque type d'épreuve.
  - Cas limites comme des fichiers JSON manquants ou des réponses invalides.

- **Résultats :**
  - Toutes les épreuves fonctionnent correctement après les ajustements.
  - Les messages d’erreur guident bien l’utilisateur en cas de problème.

---

## Difficultés principales rencontrées
1. **Gestion des fichiers JSON :**
   - Problème : Fichiers introuvables ou mal formatés.
   - **Solution :** Vérifications robustes et gestion des chemins relatifs.

2. **Validation des saisies utilisateur :**
   - Problème : Entrées non valides ou hors des choix disponibles.
   - **Solution :** Boucles et gestion des erreurs avec `try...except`.

3. **Équilibre des épreuves :**
   - Problème : Certaines épreuves basées sur le hasard semblaient trop difficiles.
   - **Solution :** Ajustement des règles pour offrir une probabilité équitable de succès.

---

## Conclusion
Le projet est maintenant complet et fonctionnel, offrant une expérience utilisateur fluide et engageante. Il a permis de mettre en pratique plusieurs concepts Python, notamment :
- Organisation modulaire.
- Gestion des fichiers JSON.
- Validation des saisies utilisateur.
- Création de jeux interactifs.

Si vous souhaitez ajouter des fonctionnalités ou améliorer certains aspects, n’hésitez pas à explorer davantage le code ou demander de l'aide !
