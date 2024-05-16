from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

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
user.send_keys('user')

password = driver.find_element(By.NAME,'session_password')
password.send_keys('pass')

login = driver.find_element(By.TAG_NAME, "button")
login.click()
sleep(2)

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

people = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")
people[0].click()
sleep(2)
driver.back()

people = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")
people[1].click()
sleep(2)
driver.back()

people = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")
people[2].click()
sleep(2)
driver.back()
