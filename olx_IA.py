import requests
from bs4 import BeautifulSoup

def buscar_concursos():
    # URL de exemplo para buscar concursos públicos
    url = "https://www.jcconcursos.com.br/concursos/inscricoes-abertas/sp"

    try:
        # Fazer a requisição para o site
        response = requests.get(url)
        response.raise_for_status()  # Verificar se a requisição foi bem-sucedida

        # Analisar o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar os concursos na página (ajuste os seletores conforme necessário)
        concursos = soup.find_all('div', class_='card-concurso')  # Exemplo de classe

        # Exibir os resultados no terminal
        print("Concursos Públicos para Técnicos em São Paulo:")
        for concurso in concursos:
            titulo = concurso.find('h3').text.strip()  # Ajuste o seletor
            detalhes = concurso.find('p').text.strip()  # Ajuste o seletor
            print(f"Título: {titulo}")
            print(f"Detalhes: {detalhes}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")

# Executar a função
buscar_concursos()
