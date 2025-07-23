from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Charger la base de mots français (fichier mots.txt requis)
with open('mots.txt', 'r', encoding='utf-8') as f:
    mots_francais = [line.strip().lower() for line in f if len(line.strip()) == 5]

# Variable pour stocker le mot secret par session
sessions = {}

def verifier_proposition(secret, proposition):
    resultat = [""] * 5
    lettres_restantes = list(secret)
    
    # Première passe: lettres correctement placées
    for i in range(5):
        if proposition[i] == secret[i]:
            resultat[i] = "correct"
            lettres_restantes[i] = None
    
    # Deuxième passe: lettres mal placées
    for i in range(5):
        if resultat[i] != "":
            continue
        if proposition[i] in lettres_restantes:
            resultat[i] = "present"
            lettres_restantes[lettres_restantes.index(proposition[i])] = None
        else:
            resultat[i] = "absent"
    
    return resultat

@app.route('/')
def index():
    # Générer un ID de session unique
    session_id = random.randint(100000, 999999)
    # Choisir un mot secret aléatoire
    sessions[session_id] = random.choice(mots_francais)
    return render_template('index.html', session_id=session_id)

@app.route('/verifier', methods=['POST'])
def verifier():
    data = request.get_json()
    proposition = data['mot'].lower()
    session_id = data['session_id']
    
    # Validation
    if len(proposition) != 5:
        return jsonify({"erreur": "Le mot doit avoir 5 lettres"}), 400
    
    if proposition not in mots_francais:
        return jsonify({"erreur": "Ce mot n'existe pas dans notre dictionnaire"}), 400
    
    # Récupérer le mot secret
    secret = sessions.get(int(session_id))
    if not secret:
        return jsonify({"erreur": "Session invalide ou expirée"}), 400
    
    # Vérifier la proposition
    resultat = verifier_proposition(secret, proposition)
    
    # Vérifier si le jeu est terminé
    victoire = proposition == secret
    fin_jeu = victoire or data['essai'] >= 5
    
    return jsonify({
        "resultat": resultat,
        "victoire": victoire,
        "fin_jeu": fin_jeu,
        "secret": secret if fin_jeu else ""
    })

if __name__ == '__main__':
    app.run(debug=True)