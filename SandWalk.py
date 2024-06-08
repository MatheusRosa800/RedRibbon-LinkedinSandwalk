# RED RIBBON - LINKEDIN FREMEN SandWalk

#integrantes: 
# Matheus Rosa
# Felipe Madeira
# Caio Vinicius
# Henrique Koji
# Pedrou Augusto

import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


def interacao(index):
    people = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")
    people[index].click()
    sleep(2)
    print("=" * 40)
    coletainfo()
    print("=" * 40)
    sleep(2)
    driver.back()

pessoas = []
    
def coletainfo():

    # NOME 
    element = driver.find_element(By.TAG_NAME, "h1")
    nome = element.text

    # # CARGO
    element = driver.find_element(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]")
    cargo = element.text

    # # LOCALIZAÇÃO
    element = driver.find_element(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]")
    local = element.text

    # SOBRE
    try:
        about = driver.find_element(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[3]/div[3]/div/div/div/span[1]")
        sobre = about.text
    except Exception:
        try:
            about = driver.find_element(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]")
            sobre = about.text
        except Exception:
            sobre = "Não há informações"

    # URL
    url = driver.current_url 

    # EXPERIENCIAS 1 
    experience = []
    elements = driver.find_elements(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[6]/div[3]/ul")
    for element in elements:
        experience.append(element.text)

    # EXPERIENCIAS 2 
    
    elements = driver.find_elements(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[7]/div[3]/ul")
    for element in elements:
        experience.append(element.text)
    
    # EXPERIENCIAS 3
    
    elements = driver.find_elements(By.XPATH, "//*[@id='profile-content']/div/div[2]/div/div/main/section[8]/div[3]/ul")
    for element in elements:
        experience.append(element.text)
        
    pessoa = [url, nome, cargo, local, sobre, experience] 
    pessoas.append(pessoa)  
    print(pessoas)

empresa = input("Por favor digite o nome da empresa alvo: ")
usuario = input("Por favor informe o usuário: ")
senha = input("Por favor informe a senha: ")

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
sleep(2)
url = "https://www.linkedin.com/feed/"
driver.get(url)
sleep(2)

user = driver.find_element(By.NAME,'session_key')
user.send_keys(usuario)

password = driver.find_element(By.NAME,'session_password')
password.send_keys(senha)

login = driver.find_element(By.TAG_NAME, "button")
login.click()
sleep(20)

search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search.click()
sleep(2)
search.send_keys(empresa)
sleep(2)
search.send_keys(Keys.ENTER)
sleep(4)

filtro = driver.find_element(By.XPATH, '//button[text()="Pessoas"]')
filtro.click()
sleep(2)

try:
    i = 0 
    while i <= 15:
        interacao(i)
        seg = random.randint(1,10)
        sleep(seg)
        i += 1

except IndexError:
    print("FIM DA CAPTURA SAMUCAO: VC FOI PWNED! - FIAP(LETS_ROCK) - FTP:C2.REDRIBBON.UK - LOGIN COMPARTILHADO ")

df = pd.DataFrame(pessoas, columns=['URL','Nome', 'Cargo', 'Local','Sobre','Experiencias'])
df.to_csv('linkedin_profiles.csv', index=False, encoding='utf-8')
print("Dados salvos com sucesso em linkedin_profiles.csv")
