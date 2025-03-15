import requests
from bs4 import BeautifulSoup

url = "https://www.webmotors.com.br/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

resposta = requests.get(url, headers = headers)

    # codigo 200 é o mesmo que sucesso
if resposta.status_code == 200:
    
    print(" requisição feita com sucesso")
    print(resposta.text)
else:
    print("deu errado")
    
   # soup = BeautifulSoup(resposta.text, "html.parser")        
    # encontrando as noticias    
    #noticias = soup.find_all("a", class_="feed-post-link")    
    #print("últimas noticias do g1:")    
    
    #for index, noticia in enumerate(noticias):
     #   print(f"{index +1}. {noticia.text.strip()} - {noticia['href']}")
              
              