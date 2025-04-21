import google.generativeai as genai
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

def verificar_post(texto):
    key = os.environ.get("api_kkey")
    prompt = 'O texto a seguir é a descrição de um post do linkedin, responda 1 caso o post seja sobre programação e não aparenta ser um post patrocinado, caso contrário ou você achar que falta informação para compreender o post responda 0: ' + texto

    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.0-flash') 
    response = model.generate_content(prompt)
    print(response.text)
    if int(response.text) == 1:
        comentar = True
    else:
        comentar = False
    return comentar

def gerar_comentario(post):
    key = os.environ.get("api_kkey")
    prompt = 'Suponha que você é um programador, faça um comentário simples e curto e que agregue sobre o seguinte post no linkedin (sem emojis)' + post 

    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.0-flash') 
    response = model.generate_content(prompt)
    return response.text


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.linkedin.com/feed/')

def realizar_login():
    sleep(2)
    login = os.environ.get("loginn")
    senha = os.environ.get("senha")
    navegador.find_element(By.XPATH, '//input[@id="username"]').send_keys(login)
    navegador.find_element(By.XPATH, '//input[@id="password"]').send_keys(senha)
    navegador.find_element(By.XPATH, '//label[@for="rememberMeOptIn-checkbox"]').click()
    navegador.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(5)


def raspar(post):
    return navegador.find_elements(By.XPATH, '//div[@class="update-components-text relative update-components-update-v2__commentary "]')[post].text


def comentar():
    sleep(2)
    for i in range(0, 5):
        if verificar_post(raspar(i)):
            texto_post = raspar(i)
            botao = navegador.find_elements(By.XPATH, '//button[@aria-label="Comentar"]')[i]
            navegador.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
            sleep(2)
            botao.click()
            sleep(1)
            input_comentarios = navegador.find_elements(By.XPATH, '//div[@contenteditable="true" and @data-placeholder="Adicionar comentário"]')
            input_comentarios[i].send_keys(gerar_comentario(texto_post))
            sleep(3)
            navegador.find_element(By.XPATH, '//button[@class="comments-comment-box__submit-button--cr artdeco-button artdeco-button--1 artdeco-button--primary ember-view"]').click()
            sleep(4)


def pesquisar(desc):
    sleep(2)
    navegador.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]').send_keys(desc)
    navegador.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]').send_keys(Keys.ENTER)


def clicar_pessoas():
    sleep(2)
    botoes = navegador.find_elements(By.XPATH, '//button[@type="button"]')
    for botao in botoes:
        if botao.text == 'Pessoas':
            botao.click()
            break


def conectar(desc):
    pesquisar(desc)
    clicar_pessoas()
    sleep(1.5)
    botoes = navegador.find_elements(By.XPATH, '//button[contains(@aria-label, "conectar")]')
    sleep(0.5)
    for botao in botoes:
        botao.click()
        sleep(1)
        navegador.find_element(By.XPATH, '//button[@aria-label="Enviar sem nota"]').click()
        sleep(1)


realizar_login()
comentar()
input()