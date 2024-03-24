# Gestionnaire de Gestes de la Main pour Emails Automatisés

Ce script utilise OpenCV et MediaPipe pour reconnaître des gestes spécifiques de la main via la webcam d'un ordinateur et envoyer des emails automatiques en fonction de ces gestes. Par exemple, un pouce levé enverra un email indiquant un message positif, tandis qu'un pouce vers le bas enverra un message négatif.

## Fonctionnalités

- Reconnaissance de gestes de la main en temps réel.
- Envoi automatique d'emails en réponse à des gestes spécifiques.
- Délai configurable entre les envois d'emails pour éviter les doublons.

## Prérequis

Pour exécuter ce script, vous aurez besoin de Python 3.6 ou supérieur et de certaines dépendances listées dans le fichier `requirements.txt`.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en exécutant la commande suivante dans votre terminal :

pip install -r requirements.txt


3. Assurez-vous de configurer les informations de l'expéditeur et du destinataire de l'email dans le script, ainsi que le mot de passe de l'email de l'expéditeur.

## Utilisation

Pour démarrer la reconnaissance des gestes, exécutez :

python gesture_email_manager.py


Positionnez votre main dans le champ de vision de la webcam. Le script reconnaîtra un pouce vers le haut ou vers le bas et enverra un email correspondant au geste détecté après un délai configurable.

## Sécurité

**Attention :** Ce script nécessite que vous entreriez votre mot de passe email directement dans le code source. Il est recommandé de créer un mot de passe d'application spécifique si vous utilisez Gmail ou tout autre fournisseur de services email qui le supporte, pour améliorer la sécurité.

## Contribution

Les contributions à ce projet sont les bienvenues. N'hésitez pas à soumettre des Pull Requests ou à ouvrir des issues pour des suggestions ou des problèmes rencontrés.

## Licence

Ce projet est distribué sous la Licence MIT. Voir le fichier `LICENSE` pour plus d'informations.


