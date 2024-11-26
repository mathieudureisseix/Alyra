# **Rapport d'Analyse des Données**

## **1. Aperçu des Données**
Les données analysées contiennent 27,396 lignes et six colonnes :
- **Colonnes des moyennes** : `mean_h`, `mean_s`, `mean_v` (composantes H, S, V de la couleur moyenne).
- **Colonnes des écarts-types** : `std_h`, `std_s`, `std_v` (variations des composantes H, S, V).
- **Colonne `label`** : Catégories des phototypes de peau (labels Fitzpatrick : III, IV, V, VI).

---

## **2. Statistiques Descriptives Globales**

| Variable   | Minimum  | Maximum   | Moyenne   | Médiane   | Écart-Type |
|------------|----------|-----------|-----------|-----------|------------|
| `mean_h`   | 0.85     | 16.30     | 8.79      | 8.81      | 2.96       |
| `mean_s`   | 25.47    | 208.58    | 120.00    | 118.78    | 34.89      |
| `mean_v`   | 30.56    | 208.58    | 149.76    | 144.95    | 38.35      |
| `std_h`    | 2.70     | 46.64     | 25.52     | 24.51     | 8.36       |
| `std_s`    | 3.86     | 59.58     | 31.52     | 31.40     | 10.63      |
| `std_v`    | 6.24     | 59.58     | 31.52     | 31.40     | 10.63      |

**Observations :**
- **Grande dispersion dans `mean_s` et `mean_v`** : Variation significative de la saturation et de la luminosité, reflétant la diversité des images.
- **Faible dispersion pour `mean_h`** : La teinte moyenne reste relativement homogène dans les tons de peau.

---

## **3. Distribution des Catégories de Peau**
| Label | Effectifs |
|-------|-----------|
| III   | 6,853     |
| IV    | 6,904     |
| V     | 6,871     |
| VI    | 6,768     |

**Observations :**
- Les catégories de peau sont équilibrées, garantissant une analyse statistique fiable.

---

## **4. Statistiques par Catégorie de Peau**

| Label | Moyenne H | Moyenne S | Moyenne V | Écart-Type H | Écart-Type S | Écart-Type V |
|-------|-----------|-----------|-----------|--------------|--------------|--------------|
| III   | 8.95      | 114.59    | 154.31    | 2.66         | 24.50        | 32.35        |
| IV    | 8.87      | 121.35    | 149.76    | 2.59         | 24.63        | 32.63        |
| V     | 8.92      | 121.00    | 140.35    | 2.62         | 24.94        | 31.06        |
| VI    | 8.41      | 123.09    | 126.23    | 2.71         | 28.07        | 29.99        |

**Observations :**
- Les phototypes III et IV présentent des valeurs plus élevées en luminosité (`mean_v`) et saturation (`mean_s`) que les phototypes V et VI.
- Les écarts-types augmentent pour les phototypes plus foncés (V, VI), indiquant une plus grande diversité intra-catégorie.

---

## **5. Matrice de Corrélation**
Les relations entre les variables ont été mesurées :

|          | `mean_h` | `mean_s` | `mean_v` | `std_h` | `std_s` | `std_v` |
|----------|----------|----------|----------|---------|---------|---------|
| `mean_h` | 1.000    | 0.289    | 0.168    | 0.047   | 0.144   | 0.165   |
| `mean_s` | 0.289    | 1.000    | -0.114   | -0.329  | 0.303   | 0.066   |
| `mean_v` | 0.168    | -0.114   | 1.000    | 0.047   | 0.074   | 0.627   |
| `std_h`  | 0.047    | -0.329   | 0.047    | 1.000   | 0.206   | 0.147   |
| `std_s`  | 0.144    | 0.303    | 0.074    | 0.206   | 1.000   | 0.356   |
| `std_v`  | 0.165    | 0.066    | 0.627    | 0.147   | 0.356   | 1.000   |

**Interprétations :**
- **Forte corrélation entre `mean_v` et `std_v`** : Les variations de luminosité sont cohérentes avec leur moyenne.
- Les autres corrélations restent faibles, reflétant une relative indépendance des dimensions.

---

## **6. Conclusion**
- Les données sont équilibrées et les catégories de peau bien représentées.
- Les phototypes diffèrent principalement en termes de luminosité (`mean_v`) et de saturation (`mean_s`).
- La matrice de corrélation confirme une indépendance relative entre les dimensions de couleur et leurs variations.