import google.generativeai as genai
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

def post_certo(texto):
    key = os.environ.get("api_kkey")
    print(f'A chave é: {key}')
    prompt = 'O texto a seguir é a descrição de um post do linkedin, responda 1 caso o post seja sobre programação e não aparenta ser um post patrocinado, caso contrário responda 0: ' + texto

    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.0-flash') # ou outro modelo válido
    response = model.generate_content(prompt)
    
    if int(response.text) == 1:
        comentar = True
    else:
        comentar = False
    return comentar

api_key = os.environ.get("api_key")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.linkedin.com/feed/')

def realizar_login():
    login = os.environ.get("loginn")
    senha = os.environ.get("senha")
    navegador.find_element(By.XPATH, '//input[@id="username"]').send_keys(login)
    navegador.find_element(By.XPATH, '//input[@id="password"]').send_keys(senha)
    navegador.find_element(By.XPATH, '//label[@for="rememberMeOptIn-checkbox"]').click()
    navegador.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(5)


def raspar(post):
    return navegador.find_elements(By.XPATH, '//div[@class="MWlvjUOSHjivEHfFstwtkXKJRLUtivOKjBYhNvo"]')[post].text

realizar_login()
print(post_certo(raspar(0)))
input()