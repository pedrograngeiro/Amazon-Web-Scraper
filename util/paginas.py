import requests
from bs4 import BeautifulSoup

def obter_numero_total_paginas(url):
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79",
                "Referer": "https://www.amazon.com.br",
                "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8",
            }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paginacao_element = soup.find("span", class_="s-pagination-item s-pagination-disabled")

        if paginacao_element:
            numero_total_paginas = int(paginacao_element.text.strip())
            return numero_total_paginas
        else:
            return 1

    else:
        print(f"Não foi possível acessar a página. Status Code: {response.status_code}")
        return None