import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"

resposta = requests.get(url)

    # codigo 200 é o mesmo que sucesso
if resposta.status_code == 200:
    
    print(" requisição feita com sucesso")
    print(resposta.text)
    
    