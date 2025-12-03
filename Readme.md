# 🏆 Mini Compétition Python : Super-Calculateur Collaboratif

Bienvenue dans ce projet collaboratif !  
L'objectif est de travailler **en équipe** de 5 apprenants, gérer **Git et GitHub**, et produire un **super-calculateur Python fonctionnel**.  

---

## **Structure du dépôt**

```
competition_repo/
│
├── README.md
├── tasks.md
├── group1/
│   ├── simple_calculator.py
│   ├── stat_calculator.py
│   └── main.py
├── group2/
│   ├── simple_calculator.py
│   ├── stat_calculator.py
│   └── main.py
├── group3/
└── group4/
```

- Chaque groupe travaille **dans son dossier** (`group1/`, `group2/`, etc.).  
- Les fichiers principaux sont :
  1. `simple_calculator.py` → 5 fonctions + boucle interactive  
  2. `stat_calculator.py` → fonctions statistiques sur les DataFrames (mod, moyenne, médiane, max/min)  
  3. `main.py` → super-calculateur combinant toutes les fonctions  

- **Tous les 4 membres contribuent à chaque fichier**,  
- **l’orchestrateur gère uniquement les pull requests, merges et tests et n’écrit pas de code.**

---

## **Répartition des rôles**

- **4 développeurs** : créent et complètent les fonctions dans les fichiers en collaboration et font les tests unitaires.  
- **1 orchestrateur** :  
  - Reçoit les pull requests  
  - Merge et rebase pour intégrer les modifications  
  - Résout les conflits si nécessaire  
  - Fait le test global de chaque fichier  
  - Teste `main.py`  

---

## **Règles de Git et collaboration**

### **Création de branche pour le groupe**
```bash
git checkout -b groupX-main
```

### **Travailler sur les fichiers**
- Modifier le fichier assigné (`simple_calculator.py`, `stat_calculator.py`, `main.py`)  
- Ajouter vos modifications :
```bash
git add simple_calculator.py
git add stat_calculator.py
git add main.py
```
- Commit avec message clair :
```bash
git commit -m "Ajout de la fonction add dans simple_calculator.py"
```
- Pousser la branche sur GitHub :
```bash
git push origin groupX-main
```

### **Pull Requests**
- Créer une PR vers la branche principale du groupe (`groupX-main`)  
- L’orchestrateur :  
  - Revoit le code  
  - Merge après validation  

### **Mettre à jour son dépôt avant de coder**
```bash
git pull origin groupX-main
```

### **Gestion des conflits**
- Si un conflit survient :
```bash
git pull --rebase origin groupX-main
# Résoudre le conflit dans l’éditeur (VS Code ou PyCharm)
git add fichier_conflit.py
git rebase --continue
```

### **Branches finales**
- Une fois toutes les fonctions terminées, l’orchestrateur merge dans :
```bash
git checkout main
git merge groupX-main
git push origin main
```

---

## **Conseils pratiques**

- Commits fréquents et descriptifs  
- Tester vos fonctions localement avant de faire un push  
- Communiquer activement pour gérer les merges et conflits  
- Respecter l’ordre de collaboration pour `simple_calculator.py` et `stat_calculator.py`  

---

## **Objectifs et critères de réussite**

- **Résultat final** : super-calculateur fonctionnel avec toutes les fonctions intégrées  
- **Collaboration** : tous les membres doivent contribuer aux fichiers (au moins 3 commits par membre)  
- **Gagnant** : le premier groupe à intégrer et tester correctement tous les fichiers avec code fonctionnel et PRs complétées  

---

## **Rappel Git & GitHub**

| Commande / Concept       | Description                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| **commit**                | Enregistrer vos modifications localement avec un message décrivant le changement.             |
| **push**                  | Envoyer vos commits locaux vers la branche correspondante sur GitHub.                          |
| **pull**                  | Récupérer les dernières modifications de la branche distante et les fusionner avec votre branche locale. |
| **branch**                | Créer une ligne de développement séparée pour travailler sur une fonctionnalité ou un groupe. |
| **checkout -b <branche>** | Créer une nouvelle branche et s’y positionner.                                                  |
| **merge**                 | Fusionner une branche dans une autre, combinant les modifications.                              |
| **rebase**                | Rejouer vos commits locaux au-dessus des commits d’une autre branche pour une histoire linéaire. |
| **pull request (PR)**     | Demander à intégrer vos changements d’une branche vers une autre sur GitHub, pour révision.   |
| **conflict**              | Erreur de fusion quand Git ne peut pas automatiquement combiner des changements incompatibles. |
| **orchestrateur**         | Personne qui reçoit les PR, merge ou rebase, résout les conflits et teste le code intégré.    |
