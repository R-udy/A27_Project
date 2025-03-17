import asyncio
import httpx  # Alternative asynchrone à requests

class ClientA27:
    def __init__(self, timeout=5):
        # 10s avant timeout
        self.timeout = timeout  # Délai maximal pour les requêtes
        self.client = httpx.AsyncClient(timeout=self.timeout)

    async def requeter(self, url):
        """Effectue une requête HTTP GET à l'URL donnée de manière asynchrone"""
        try:
            response = await self.client.get(url)
            return response
        except httpx.HTTPStatusError as http_err:
            return f"Erreur HTTP pour {url}: {http_err}"
        except httpx.RequestError as req_err:
            return f"Erreur de connexion pour {url}: {req_err}"
        except Exception as e:
            return f"Erreur inconnue pour {url}: {e}"

    async def close(self):
        """Ferme le client HTTP proprement"""
        await self.client.aclose()


# Fonction principale pour exécuter des requêtes
async def main():
    client = ClientA27()



    # Appel à la méthode requeter pour chaque URL
    for url in urls:
        response = await client.requeter(url)
        
        # Affichage de la réponse
        if isinstance(response, str):  # Cas d'erreur
            print(response)
        else:
            print(f"Réponse de {url}: {response.text}")

    # Fermeture propre du client HTTP après utilisation
    await client.close()


# Lancer le programme asynchrone
if __name__ == '__main__':
    asyncio.run(main())
