import json
import time


class GestionnaireScenarios:
    def __init__(self, chemin_fichier_config, client):
        self.config = self.lire_fichier_config(chemin_fichier_config)
        self.client = client

    def lire_fichier_config(self, chemin_fichier_config):
        with open(chemin_fichier_config, "r") as fichier:
            return json.load(fichier)

    def executer(self, cle_scenario):
        for step in self.config["scenarios"][cle_scenario][('steps')]:
            if step['action'] == 'http_request_get':
                url = step['url']
                self.client.requeter(url)
            elif step['action'] == 'pause':
                duree = step['duration'] / 1000
                time.sleep(duree)
        
        

    def lancer_sequence(self, id):
        if id == 42:
            self.executer('42')
            
        
