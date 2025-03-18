from bottle import route, run, request, response, static_file
import json

# État initial de l'ampoule (éteinte) et de l'alarme (désactivée)
ampoule_allumee = True
alarme_activee = False

# Route pour afficher la page d'accueil avec le dessin de l'ampoule et de l'alarme
@route('/')
def index():
    return static_file("index.html", root=".")

# Route pour récupérer l'état de l'ampoule
@route('/etat_ampoule')
def etat_ampoule():
    response.content_type = 'application/json'
    return json.dumps({'allumee': ampoule_allumee})

# Route pour récupérer l'état de l'alarme
@route('/etat_alarme')
def etat_alarme():
    response.content_type = 'application/json'
    return json.dumps({'activee': alarme_activee})

# Route pour allumer ou éteindre l'ampoule
@route('/allumer_eteindre', method='POST')
def allumer_eteindre():
    global ampoule_allumee
    ampoule_allumee = not ampoule_allumee  # Inversion de l'état de l'ampoule
    return ''

# Route pour activer ou désactiver l'alarme
@route('/activer_desactiver', method='POST')
def activer_desactiver():
    global alarme_activee
    alarme_activee = not alarme_activee  # Inversion de l'état de l'alarme
    return ''

if __name__ == '__main__':
    run(host='192.168.190.21', port=8181)
