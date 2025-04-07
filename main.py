import google.generativeai as genai
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

login = os.environ.get("login")
senha = os.environ.get("senha")
api_key = os.environ.get("api_key")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.linkedin.com/feed/')