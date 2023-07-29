import os.path

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

    soup = BeautifulSoup(page.content, "html.parser")

    # Encontre todos os elementos com a classe "a-size-base-plus a-color-base a-text-normal"
    titles = soup.find_all(class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
    prices = soup.find_all(class_="a-price")

    # Loop para extrair o texto de cada elemento encontrado
    # for title_element in titles:
    #     title = title_element.get_text().strip()
    #
    #     gerar_csv.append_to_csv(title, )
    #     print(title)
    for idx, title_element in enumerate(titles):
        title = title_element.get_text().strip()
        price_element = prices[idx]
        price = price_element.get_text().strip()

        if not os.path.exists("AmazonWebScraping.csv"):
            gerar_csv.write_to_csv(title, price)
            gerar_csv.append_to_csv(title, price)
        else:
            gerar_csv.append_to_csv(title, price)

        print(f'Title: {title}, Price: {price}')