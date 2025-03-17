import unittest

import time

from gestionnaire_scenarios import GestionnaireScenarios

# Ce test s'appuie sur un fichier test_scenarios.json
class TestGestionnaireScenarios(unittest.TestCase):
    def setUp(self):
        self.client_stub = ClientStub()
        self.gestionnaire_scenarios = GestionnaireScenarios("./test_scenarios.json", self.client_stub)

    def test_executer_sequence(self):
        self.gestionnaire_scenarios.executer("42")
        self.assertEqual(len(self.client_stub.requetes_recues), 2, "Nombre de requetes incorrect")
        requete1 = self.client_stub.requetes_recues[0]
        requete2 = self.client_stub.requetes_recues[1]
        # Vérifier que la première requête contient le texte '4201'
        self.assertRegex(requete1['requete'], "4201")
        # Vérifier que la deuxième requête contient le texte '4202'
        self.assertRegex(requete2['requete'], "4202")
        # Vérifier que la durée de pause entre les deux appels à requeter est de deux secondes, à 0.1 secondes prêt
        self.assertAlmostEqual(requete2['timestamp'] - requete1['timestamp'], 2, delta = 0.1)
    def test_lancer_sequence_success(self):
        self.assertIsNone(self.gestionnaire_scenarios.lancer_sequence(42))    
        
    def test_lancer_sequence_failed(self):
        with self.assertRaises(ValueError):
            self.gestionnaire_scenarios.lancer_sequence(15)
    
class ClientStub:
    def __init__(self):
        self.t0 = time.time()
        self.requetes_recues = []
    def requeter(self, requete):
        rel_t = time.time() - self.t0
        timestamp_requete = {"timestamp":rel_t, "requete":requete}
        self.requetes_recues.append(timestamp_requete)
        

if __name__ == "__main__":
    unittest.main()