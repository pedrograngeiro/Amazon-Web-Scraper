# import libraries

# import libraries util
from util import extrator

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

# Conenect to the website
URL = "https://www.amazon.com.br/Headphone-Ouvido-HV-H2002d-Microfone-Falante/dp/B07Y2G7VX5?ufe=app_do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79",
    "Referer": "https://www.amazon.com.br",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8",
}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = extrator.pegar_texto_id(soup2, "productTitle")
price = extrator.pegar_texto_classe(soup2, "a-offscreen")

