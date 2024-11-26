import cv2
from matplotlib import pyplot as plt
import os

# Chemin vers l'image
base_dir = "../Dataset/Photos"  # Remonter au niveau du répertoire parent
image_subdir = "train"
image_name = "1.jpg"
image_path = os.path.join(base_dir, image_subdir, image_name)

# Vérifier que l'image existe
if not os.path.exists(image_path):
    print(f"Erreur : l'image {image_name} n'existe pas dans {os.path.join(base_dir, image_subdir)}")
else:
    # Charger l'image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir en niveaux de gris pour la détection

    # Charger le classifieur Haar Cascade pour la détection de visage
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Détecter les visages
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Bleu pour les rectangles

    # Convertir en RGB pour l'affichage avec Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Afficher l'image avec les rectangles autour des visages
    plt.imshow(image_rgb)
    plt.title(f"Visages détectés dans {image_name}")
    plt.axis("off")
    plt.show()

    # Si aucun visage n'est détecté
    if len(faces) == 0:
        print("Aucun visage détecté dans cette image.")