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

##  Lancer le projet

- Cloner le répo
- exécuter le fichier app.py
```bash
python3 app.py
```
- ouvrir la page web locale


