# Fichier pour le pretraitement des images echographiques du coeur


# Creation d'un mask binaire du cone pour ignorer le fond noir de l'image echographique.

# Extraction du signal ECG.

# Crop automatique pour enlever les bords noirs inutiles, pour reduire la taille la taille du coeur et donc de le centrer dans l'image.

# Amelioration du contraste local avec CLAHE.

# Filtre median / bilaterale pour reduire le speckle ultrasound.

# Masquer le signal ECG si il est present pour ne pas qu'il puisse gener la segmentation.