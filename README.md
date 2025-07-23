# Wordle en français avec Flask 

Ce projet est une version web du jeu **Wordle** en français (Motus), développée en Python avec le framework **Flask**.

## Règles du jeu

L'utilisateur a 6 tentatives pour trouver un mot de 5 lettres de la langue française. Les mots sont contenus dans le fichier mots.txt qui provient de la page web : https://www.listesdemots.net/mots5lettres.htm  
Les lettres s'affichent en orange si elles sont dans le mot mais mal placées et en vert si elles sont dans le mot et bien placées.   
Si l'utilisateur ne trouve pas le mot après la dernière tentative, le mot secret lui est révélé. 

## Prérequis pour l'exécution (flask)
```bash
pip install flask
```
Utilisation de chatgpt afin de comprendre comment utiliser flask

##  Lancer le projet

- Cloner le répo
- exécuter le fichier app.py
```bash
python3 app.py
```
- ouvrir la page web locale

## Difficultés rencontrées

Voici quelques exemples de problèmes rencontrés et leurs solutions :

- **Fichier `mots.txt` mal formaté**
  - Problème : les mots étaient séparés par des espaces au lieu d’un mot par ligne.
  - Solution : script Python pour reformater automatiquement le fichier.

- **Erreur `TemplateNotFound`**
  - Problème : le fichier `index.html` n’était pas dans le dossier `templates` alors qu'il devait l'être en raison de l'utilisation de flask.
  - Solution : création d’un dossier `templates/` à la racine et déplacement du fichier dedans. (solution expliquée par chatgpt)

- **Variables Flask manquantes**
  - Problème : erreurs sur `session_id` non défini ou erreurs de route.
  - Solution : ajout de `session_id = str(uuid4())` dans la route `/`.

- **Logique de vérification des lettres**
  - Problème : prise en compte incorrecte de lettres bien placées vs mal placées.
  - Solution : réécriture de la boucle de validation.

Nathan Weisman, 1A

