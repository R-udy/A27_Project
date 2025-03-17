import asyncio  # Module pour la gestion des opérations asynchrones
import threading  # Module pour la gestion des threads
import sys  # Module pour interagir avec l'interpréteur Python
from client import ClientA27  # Importation d'une classe ClientA27 définie dans un autre fichier
from bottle import Bottle, run  # Framework web léger pour créer un serveur
from gestionnaire_scenarios import GestionnaireScenarios  # Importation d'une classe pour gérer les scénarios

class ServeurA27(Bottle):
    """
    Classe représentant un serveur basé sur Bottle, qui écoute les requêtes et déclenche des scénarios.
    """

    def __init__(self, gestionnaire_sequence):
        """
        Initialise le serveur en enregistrant une route pour gérer les requêtes.

        :param gestionnaire_sequence: Instance de GestionnaireScenarios permettant de gérer les scénarios.
        """
        Bottle.__init__(self)  # Initialisation de la classe Bottle
        self.gestionnaire_sequence = gestionnaire_sequence
        self.route("/<id:int>", callback=self.gerer_requete)  # Définition d'une route dynamique prenant un ID entier

    def gerer_requete(self, id):
        """
        Gère les requêtes entrantes et déclenche la séquence correspondante.

        :param id: Identifiant du scénario à exécuter.
        """
        self.gestionnaire_sequence.lancer_sequence(id)  # Appel de la méthode pour lancer la séquence

    def demarrer(self):
        """
        Démarre le serveur web dans un thread séparé pour ne pas bloquer l'exécution principale.
        """
        mon_thread = threading.Thread(target=run, kwargs={'app': self, 'host': '0.0.0.0', 'port': 8081})
        mon_thread.daemon = True  # Rend le thread daemon pour qu'il se termine avec le programme principal
        mon_thread.start()  # Démarrage du thread
        return mon_thread  # Retourne le thread en cours d'exécution


if __name__ == '__main__':
    # Initialisation du client
    client = ClientA27()
    
    # Chargement du gestionnaire de scénarios avec un fichier JSON
    gestionnaire = GestionnaireScenarios('test_scenarios.json', client)
    
    # Création et démarrage du serveur
    serveur = ServeurA27(gestionnaire)
    serveur.demarrer()
