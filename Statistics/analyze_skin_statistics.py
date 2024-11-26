import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV généré précédemment
csv_path = "cleaned_skin_statistics.csv"
df = pd.read_csv(csv_path)

# Vérifier la structure des données
print("Aperçu des données :")
print(df.head())

# Statistiques générales par colonne
print("\nStatistiques descriptives globales :")
print(df.describe())

# Distribution des labels (phototypes)
print("\nDistribution des catégories de peau :")
label_counts = df['label'].value_counts()
print(label_counts)

# Visualiser la distribution des labels
plt.figure(figsize=(8, 6))
label_counts.plot(kind='bar', color='skyblue')
plt.title("Distribution des catégories de peau")
plt.xlabel("Label (Phototype)")
plt.ylabel("Nombre d'images")
plt.xticks(rotation=0)
plt.show()

# Statistiques par catégorie de peau
print("\nStatistiques par catégorie de peau :")
grouped = df.groupby('label').mean()
print(grouped)

# Visualiser les moyennes HSV par catégorie de peau
plt.figure(figsize=(12, 6))
for column in ['mean_h', 'mean_s', 'mean_v']:
    grouped[column].plot(kind='bar', alpha=0.7, label=column)

plt.title("Moyennes HSV par catégorie de peau")
plt.xlabel("Label (Phototype)")
plt.ylabel("Valeurs moyennes HSV")
plt.legend()
plt.xticks(rotation=0)
plt.show()

# Matrice de corrélation entre les colonnes
correlation_matrix = df[['mean_h', 'mean_s', 'mean_v', 'std_h', 'std_s', 'std_v']].corr()
print("\nMatrice de corrélation :")
print(correlation_matrix)

# Visualiser la matrice de corrélation
plt.figure(figsize=(8, 6))
plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)
plt.colorbar()
plt.title("Matrice de corrélation entre les caractéristiques", pad=20)
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.show()