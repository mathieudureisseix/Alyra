import cv2
import numpy as np
import os

# Chemin de base pour les répertoires des données
base_dir = "../Dataset/Photos"
image_subdir = "train"
image_name = "1.jpg"
image_path = os.path.join(base_dir, image_subdir, image_name)

# Vérifier que l'image existe
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
            skin_region = cv2.bitwise_and(hsv_roi, hsv_roi, mask=skin_mask)

            # Calculer les statistiques des couleurs (moyenne et écart type)
            mean_hsv = cv2.mean(hsv_roi, mask=skin_mask)[:3]
            std_hsv = cv2.meanStdDev(hsv_roi, mask=skin_mask)

            # Afficher les statistiques
            print(f"Moyenne HSV : {mean_hsv}")
            print(f"Écart type HSV : {std_hsv[1].flatten()}")

            # Afficher la région de peau et le masque
            cv2.imshow("Skin Region", skin_region)
            cv2.waitKey(0)
            cv2.destroyAllWindows()