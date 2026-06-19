
    NOM1 PRENOM1 - NOM2 PRENOM2

## Introduction
    - Objectifs
    - Description donnees

Notre objectif est de repérer le nombre de cycles cardiaques, les phases de systole et diastole, et d'afficher l'évolution des volumes des ventricules et atriums au cours du temps. Pour cela, nous allons utiliser les images fournies dans le projet.

Les images sont des images échographiques du coeur, avec un signal ECG en bas de l'image en vert. Les images sont fournies dans un dossier "data".

## Idee de la marche a suivre

### Premiere idee :

Les premieres idee que nous avons penser en debutant ce projet et apres quelques recherches pour atteindre le resultat souhaite, serait :
- Tout d'abord de pretraiter les images pour les rendre plus facile a manipuler (extraire seulement les zones "utiles" du coeur, et le signal present sur toutes les images).
- Ensuite, de segmenter les images pour identifier les differentes structures du coeur.
- Puis, de detecter les cycles cardiaques et identifier les phases systoliques et diastoliques.
- Enfin, d'estimer les volumes des ventricules et atriums au cours du temps et de les afficher sous forme de courbes.

Nous pensons utiliser le signal present sur les images pour faire valider nos resultats et pour identifier les cycles cardiaques. Nous pensons aussi utiliser des methodes de machine learning pour la segmentation des images.



### Idee finale :

...

## Anotation + Definitions des termes

LV = ventricule gauche
RV = ventricule droit
LA = atrium gauche
RA = atrium droit
septum interventriculaire
valves mitrale et tricuspide
parois myocardiques

Dyastole = phase de relaxation du coeur, pendant laquelle les ventricules se remplissent de sang.
Systole = phase de contraction du coeur, pendant laquelle les ventricules se vident de leur sang.

![Heart_Image](https://www.fedecardio.org/wp-content/uploads/2021/03/schema-valves_0.jpg)

## Pretraitement

crop automatique pour enlever les bords noirs inutiles
CLAHE pour améliorer le contraste local
filtre médian / bilatéral pour réduire le speckle ultrasound
éventuellement suppression de la trace ECG si elle gêne la segmentation

## Segmentation

## Estimation des volumes

## Detection des cycles cardiaques

## Resultats

## Validation

## Limites

## Conclusion