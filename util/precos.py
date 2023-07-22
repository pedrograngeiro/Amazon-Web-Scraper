from bs4 import BeautifulSoup
from util import extrator
from util import gerar_csv
import requests

def check_price(url):
    URL = url

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

    price = price.strip()[1:]
    title = title.strip()

    gerar_csv.append_to_csv(title, price)
