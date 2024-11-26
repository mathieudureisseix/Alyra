import cv2
from matplotlib import pyplot as plt
import os
import numpy as np

# Chemin de base pour les répertoires des données
base_dir = "../Dataset/Photos"
image_subdir = "train"
image_name = "1.jpg"
image_path = os.path.join(base_dir, image_subdir, image_name)

# Vérification de l'existence de l'image
if not os.path.exists(image_path):
    print(f"Erreur : l'image {image_name} n'existe pas dans {os.path.join(base_dir, image_subdir)}")
else:
    # Charger l'image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Charger le classifieur Haar Cascade pour la détection de visage
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Détecter les visages
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Vérifier si des visages sont détectés
    if len(faces) == 0:
        print("Aucun visage détecté dans cette image.")
    else:
        for (x, y, w, h) in faces:
            # Extraire la région du visage
            face_roi = image[y:y+h, x:x+w]

            # Convertir en espace HSV
            hsv_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2HSV)

            # Définir les seuils pour la couleur de peau dans l'espace HSV
            lower_skin = np.array([0, 20, 70], dtype=np.uint8)
            upper_skin = np.array([20, 255, 255], dtype=np.uint8)

            # Appliquer un masque pour extraire la peau
            skin_mask = cv2.inRange(hsv_roi, lower_skin, upper_skin)
            skin_region = cv2.bitwise_and(face_roi, face_roi, mask=skin_mask)

            # Afficher les résultats
            plt.subplot(1, 2, 1)
            plt.imshow(cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB))
            plt.title("Visage détecté")
            plt.axis("off")

            plt.subplot(1, 2, 2)
            plt.imshow(cv2.cvtColor(skin_region, cv2.COLOR_BGR2RGB))
            plt.title("Région de la peau")
            plt.axis("off")

            plt.show()