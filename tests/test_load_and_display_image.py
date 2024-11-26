import cv2
from matplotlib import pyplot as plt
import os

# Chemin de base pour les répertoires des données
base_dir = "../Dataset/Photos"  # Remonter au niveau du répertoire parent
image_subdir = "train"  # Sous-dossier
image_name = "1.jpg"

# Construction du chemin complet vers l'image
image_path = os.path.join(base_dir, image_subdir, image_name)

# Vérification de l'existence du fichier
if not os.path.exists(image_path):
    print(f"Erreur : l'image {image_name} n'existe pas dans {os.path.join(base_dir, image_subdir)}")
else:
    # Chargement de l'image avec OpenCV
    image = cv2.imread(image_path)

    # Conversion en RGB (OpenCV charge les images en BGR par défaut)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Affichage avec Matplotlib
    plt.imshow(image_rgb)
    plt.title(f"Image : {image_name}")
    plt.axis("off")
    plt.show()