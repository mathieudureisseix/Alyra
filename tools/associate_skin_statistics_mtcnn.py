import pandas as pd
import cv2
import numpy as np
import os
from mtcnn import MTCNN  # Importer le détecteur MTCNN

# Chemins des fichiers et répertoires
csv_path = "../Dataset/train_final.csv"  # Chemin vers le fichier CSV contenant les labels
base_dir = "../Dataset/Photos"  # Répertoire contenant les images
image_subdir = "train"  # Sous-dossier des images (par exemple, train, val)

# Charger les labels à partir du fichier CSV
labels_df = pd.read_csv(csv_path)

# Initialiser MTCNN pour la détection des visages
detector = MTCNN()

# Initialiser une liste pour stocker les données
data = []

# Créer des fichiers de log pour les images problématiques
failed_images_log = "failed_images.txt"
no_faces_detected_log = "no_faces_detected.txt"
unlabeled_images_log = "unlabeled_images.txt"

# Vider les fichiers de log au début
open(failed_images_log, "w").close()
open(no_faces_detected_log, "w").close()
open(unlabeled_images_log, "w").close()

# Parcourir toutes les images dans le répertoire spécifié
image_folder = os.path.join(base_dir, image_subdir)
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)

    # Vérifier que l'image existe et est lisible
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erreur : Impossible de charger l'image '{image_name}' depuis '{image_path}'.")
        with open(failed_images_log, "a") as f:
            f.write(image_name + "\n")
        continue

    # Convertir en RGB (MTCNN attend des images en RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Détecter les visages avec MTCNN
    faces = detector.detect_faces(image_rgb)

    if len(faces) == 0:
        print(f"Aucun visage détecté dans l'image {image_name}.")
        with open(no_faces_detected_log, "a") as f:
            f.write(image_name + "\n")
        continue

    for face in faces:
        # Récupérer les coordonnées du visage détecté
        x, y, w, h = face['box']

        # Extraire la région du visage
        face_roi = image[y:y+h, x:x+w]

        # Convertir en espace HSV
        hsv_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2HSV)

        # Définir les seuils pour la peau dans l'espace HSV
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)

        # Appliquer un masque pour extraire la peau
        skin_mask = cv2.inRange(hsv_roi, lower_skin, upper_skin)

        # Calculer les statistiques (moyenne et écart type)
        mean_hsv = cv2.mean(hsv_roi, mask=skin_mask)[:3]
        std_hsv = cv2.meanStdDev(hsv_roi, mask=skin_mask)[1].flatten()

        # Récupérer le label (phototype) à partir du CSV
        label_row = labels_df.loc[labels_df['file'] == image_name]
        if label_row.empty:
            print(f"Label introuvable pour {image_name} dans le CSV.")
            with open(unlabeled_images_log, "a") as f:
                f.write(image_name + "\n")
            continue
        label = label_row['phototype'].values[0]

        # Ajouter les données dans la liste
        data.append({
            "image": image_name,
            "mean_h": mean_hsv[0],
            "mean_s": mean_hsv[1],
            "mean_v": mean_hsv[2],
            "std_h": std_hsv[0],
            "std_s": std_hsv[1],
            "std_v": std_hsv[2],
            "label": label
        })

# Convertir les données en DataFrame
df = pd.DataFrame(data)

# Afficher un aperçu des données
print(df.head())

# Sauvegarder les données dans un fichier CSV
output_csv_path = "skin_statistics_with_labels_mtcnn.csv"
df.to_csv(output_csv_path, index=False)
print(f"Données enregistrées dans '{output_csv_path}'.")