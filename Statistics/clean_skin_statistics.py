import pandas as pd
import numpy as np

# Définir les colonnes nécessaires
NUMERIC_COLUMNS = ['mean_h', 'mean_s', 'mean_v', 'std_h', 'std_s', 'std_v']
LABEL_COLUMN = 'label'

# Chemins des fichiers
INPUT_CSV = "../tools/skin_statistics_with_labels_mtcnn.csv"
OUTPUT_CSV = "cleaned_skin_statistics.csv"

def load_data(file_path):
    """
    Charge les données à partir d'un fichier CSV.
    """
    print("Chargement des données...")
    return pd.read_csv(file_path)

def filter_columns(df):
    """
    Garde uniquement les colonnes nécessaires : colonnes numériques et labels.
    """
    print("\nÉtape 1 : Filtrer les colonnes nécessaires")
    required_columns = NUMERIC_COLUMNS + [LABEL_COLUMN]
    df = df[required_columns]
    return df

def handle_non_numeric(df):
    """
    Convertit les colonnes numériques en float et gère les erreurs.
    """
    print("\nÉtape 2 : Conversion des colonnes numériques")
    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def handle_missing_values(df):
    """
    Gère les valeurs manquantes en remplaçant par la moyenne des colonnes.
    """
    print("\nÉtape 3 : Gestion des valeurs manquantes")
    for column in NUMERIC_COLUMNS:
        if df[column].isnull().sum() > 0:
            mean_value = df[column].mean()
            print(f"Remplacement des NaN dans '{column}' par la moyenne ({mean_value:.2f})")
            df[column].fillna(mean_value, inplace=True)
    return df

def remove_outliers(df):
    """
    Supprime les valeurs aberrantes en utilisant l'écart interquartile (IQR).
    """
    print("\nÉtape 4 : Gestion des valeurs aberrantes (outliers)")
    for column in NUMERIC_COLUMNS:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        print(f"Suppression des outliers dans '{column}' : [{lower_bound:.2f}, {upper_bound:.2f}]")
        df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
        df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    return df

def validate_labels(df):
    """
    Vérifie que les labels sont valides et supprime les lignes avec des labels invalides.
    """
    print("\nÉtape 5 : Validation des labels")
    valid_labels = ['I', 'II', 'III', 'IV', 'V', 'VI']  # Ajouter les labels attendus
    df = df[df[LABEL_COLUMN].isin(valid_labels)]
    return df

def save_cleaned_data(df, output_file):
    """
    Sauvegarde les données nettoyées dans un fichier CSV.
    """
    print("\nSauvegarde des données nettoyées...")
    df.to_csv(output_file, index=False)
    print(f"Données nettoyées enregistrées dans '{output_file}'.")

def main():
    # Charger les données
    df = load_data(INPUT_CSV)

    # Pipeline de nettoyage
    df = filter_columns(df)
    df = handle_non_numeric(df)
    df = handle_missing_values(df)
    df = remove_outliers(df)
    df = validate_labels(df)

    # Sauvegarder le fichier nettoyé
    save_cleaned_data(df, OUTPUT_CSV)

    # Aperçu des données nettoyées
    print("\nAperçu des données nettoyées :")
    print(df.head())
    print("\nStatistiques descriptives des colonnes numériques :")
    print(df[NUMERIC_COLUMNS].describe())

if __name__ == "__main__":
    main()