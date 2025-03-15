from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do navegador
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Rodar sem interface gráfica
driver = webdriver.Chrome(options=options)

try:
    # Acessar o site OLX
    driver.get("https://www.olx.com.br/")

    # Aguardar a barra de pesquisa carregar
    search_box = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='O que você procura?']"))
    )
    search_box.send_keys("Impressora Ender V3")
    search_box.send_keys(Keys.RETURN)

    # Aguardar os anúncios carregarem
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'sc-1fcmfeb-2')]"))
    )

    # Capturar os títulos e preços
    anuncios = driver.find_elements(By.XPATH, "//h2[@class='sc-1bofr6e-5']")
    precos = driver.find_elements(By.XPATH, "//span[@class='sc-ifAKCX fyxZlK']")

    # Exibir os resultados no terminal
    print("Resultados encontrados para 'Impressora Ender V3':")
    for anuncio, preco in zip(anuncios[:10], precos[:10]):  # Limitar aos 10 primeiros resultados
        print(f"Anúncio: {anuncio.text.strip()} - Preço: {preco.text.strip()}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador
    driver.quit()
