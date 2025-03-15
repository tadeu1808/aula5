from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Moxilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTMKL, like Gecko) Chrome/91.0.4472.124 Safari537.36')

driver = webdriver.Chrome(options=options)

url = 'https://www.webmotors.com.br/carros/sp/honda/city?tipoveiculo=carros&estadocidade=S%C3%A3o%20Paulo&marca1=HONDA&modelo1=CITY&lkid=1022&page=1'

driver.get(url)

time.sleep(5)

carros = driver.find_element(By.CLASS_NAME, '_Container')