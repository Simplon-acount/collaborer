# 📝 Tâches Python - Compétition Collaborative (Super-Calculateur)

Chaque groupe travaille sur **3 fichiers principaux** :  

1. `simple_calculator.py`  
2. `stat_calculator.py`  
3. `main.py`  

**Tous les 4 membres contribuent à chaque fichier**, puis l’orchestrateur gère **pull requests, merges et tests**.

---

## **Répartition des sous-tâches par fichier**

### **simple_calculator.py**
- Tâches individuelles (chacun complète au moins 1-2 fonctions) :
  1. Créer une fonction `add(a, b)`  
  2. Créer une fonction `subtract(a, b)`  
  3. Créer une fonction `multiply(a, b)`  # utiliser la fonction `add(a, b)` 
  4. Créer une fonction `divide(a, b)` (gestion division par zéro)  
  5. Créer une fonction `power(a, b)`  # utiliser la fonction `multiply(a, b)`
- Ajouter une **boucle interactive** permettant à l’utilisateur de choisir une opération et saisir les nombres.  

### **stat_calculator.py**
- Tâches individuelles :
  6. Créer une fonction `normalise(df)` → retourne le dataframe normalisé
  7. Créer une fonction `mod(df1, df2)` → retourne le mode de `df1` et le mode de `df2`  
  8. Créer une fonction `averageMed(df)` → retourne la moyenne et la médiane de `df`  
  9. Créer une fonction `moreDispersed(df1, df2)` → retourne quel DataFrame est le plus dispersé après normalisation (utiliser `normalise(df)`)  
  10. Créer une fonction `maxMin(numbers)` → retourne le maximum et le minimum d’une liste  
  11. Créer une fonction combinant toutes les fonctions précédentes pour un calcul avancé (`dfStats`) → utilise les 4 fonctions précédentes  

### **main.py**
- Tâches individuelles :
  12. Importer toutes les fonctions de `simple_calculator.py` et `stat_calculator.py`  
  13. Créer une interface complète (super-calculateur) qui utilise toutes les fonctions précédentes et affiche un résumé interactif des résultats  

---

## **Règles Git et collaboration**

1. **Tous les membres travaillent sur la même branche du groupe** :
   ```bash
   git checkout -b groupX-main
   ```
2. Chaque membre fait ses modifications sur `simple_calculator.py`, `stat_calculator.py` ou `main.py`.  
3. **Commits et push fréquents** pour éviter les conflits :
   ```bash
   git add simple_calculator.py stat_calculator.py main.py
   git commit -m "Ajout fonction X"
   git push origin groupX-main
   ```
4. **Orchestrateur** :
   - Reçoit les pull requests  
   - Merge ou rebase pour intégrer les modifications  
   - Résout les conflits si nécessaire  
   - Teste `main.py` pour s’assurer que tout fonctionne  

---

## **Objectif final et critères de réussite**

- Chaque groupe doit avoir un **super-calculateur fonctionnel** avec toutes les fonctions intégrées.  
- Les 4 membres doivent avoir contribué à chaque fichier.  
- L’**orchestrateur** ne code pas mais s’assure que **le code des membres est correctement intégré**.  
- **Gagnant** : le premier groupe à intégrer et tester correctement tous les fichiers avec code fonctionnel et PRs complétées.
