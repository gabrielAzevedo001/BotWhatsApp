import traceback
from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define o diretório do perfil do usuário do Chrome
dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + os.path.join(dir_path, "profile", "zap"))

# Inicia o navegador Chrome com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

# Acessando o WhatsApp Web
driver.get("https://web.whatsapp.com/")
time.sleep(20)

texto = "Opa tudo de boa?"
lista_conversas = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

for conversa in lista_conversas:
    try:
        #
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='listitem']")))
        conversa.click()
        time.sleep(5)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Type a message'], div[title='Digite uma mensagem']")))
        # Determino que caixa_texto procure pelo elemento title='Type a message'] ou pelo div[title='Digite uma mensagem']
        caixa_texto = driver.find_element(By.CSS_SELECTOR, "div[title='Type a message'], div[title='Digite uma mensagem']")
        caixa_texto.click()
        time.sleep(5)
        caixa_texto.send_keys(texto)
        time.sleep(5)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Enviar']")))
        botao_enviar = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Enviar']")
        botao_enviar.click()
        print("Mensagem enviada")
        time.sleep(5)
    except Exception:
        print("Erro ao enviar a mensagem")
        traceback.print_exc()

driver.quit()
