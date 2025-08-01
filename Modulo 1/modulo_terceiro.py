print("\nImportação e uso de um módulo de terceiros")
import requests 

url = "https://www.example.com"
reponse = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status code: {reponse.status_code}")