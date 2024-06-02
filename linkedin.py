from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
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

    pessoa = [nome, cargo, local] 

    # EXPERIENCE

    # FORM ACADEMICA

    pessoas.append(pessoa)  
    print(pessoas)

empresa = "fiap"

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
sleep(2)
url = "https://www.linkedin.com/feed/"
driver.get(url)
sleep(2)

user = driver.find_element(By.NAME,'session_key')
user.send_keys('carlosfiliano@gmail.com')

password = driver.find_element(By.NAME,'session_password')
password.send_keys('(QbAE&*6j7#U!@AsnR%K(9mZEWFvTz=[Gfj')

login = driver.find_element(By.TAG_NAME, "button")
login.click()
sleep(10)

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

interacao(0)
interacao(1)
interacao(2)

df = pd.DataFrame(pessoas, columns=['Nome', 'Cargo', 'Local'])
print(df)
