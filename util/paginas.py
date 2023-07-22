import requests
from bs4 import BeautifulSoup

def obter_numero_total_paginas(url, print_info=False):
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
            # Imprimindo informações se print_info for True
            if print_info:
                print(f"Total de páginas encontradas: {numero_total_paginas}")
            return numero_total_paginas
        else:
            # Imprimindo informações se print_info for True
            if print_info:
                print("Nenhuma página encontrada. Retornando 1 página.")
            return 1

    else:
        print(f"Não foi possível acessar a página. Status Code: {response.status_code}")
        return None

def navegar_entre_paginas(url, numero_pagina, print_info=False):
    if numero_pagina < 1:
        numero_pagina = 1

    url_partes = url.split("&page=")
    base_url = url_partes[0]
    pagina_param = f"&page={numero_pagina}"
    url_navegada = f"{base_url}{pagina_param}"

    # Imprimindo informações se print_info for True
    if print_info:
        print(f"Navegando para a página {numero_pagina}: {url_navegada}")

    return f"{base_url}{pagina_param}"

def obter_lista_urls_paginas(url, numero_total_paginas, print_info=False):
    lista_urls = []
    for numero_pagina in range(1, numero_total_paginas + 1):
        url_pagina = navegar_entre_paginas(url, numero_pagina, print_info=print_info)
        lista_urls.append(url_pagina)
    return lista_urls