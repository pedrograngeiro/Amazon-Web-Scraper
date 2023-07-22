import time
from util.precos import check_price
from util import paginas
from util.paginas import obter_lista_urls_paginas
from util.paginas import obter_numero_total_paginas

def rodando_checkagem_de_precos():
    termo_de_pesquisa = "monitor"
    url_pesquisa = f"https://www.amazon.com.br/s?k={termo_de_pesquisa.replace(' ', '+')}"

    total_paginas = obter_numero_total_paginas(url_pesquisa)
    numero_da_pagina = paginas.obter_lista_urls_paginas(url_pesquisa, total_paginas, print_info=True)

    # while True:
    #     url = "https://www.amazon.com.br/Monitor-AOC-G-Sync-Compatible-27G2/dp/B088L3TM7X/ref=sr_1_1?pf_rd_i=16364756011&pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_p=3a4566d3-19f5-4330-ba47-df1b7bbd88a2&pf_rd_r=TBJX7096TP23B8K7MYV4&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1689553216&s=computers&sr=1-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
    #     check_price(url)
    #     time.sleep(20)

    # df = pd.read_csv("AmazonWebScraping.csv")
    # print(df)
def run():
    termo_de_pesquisa = "monitor "
    # url_pesquisa = f"https://www.amazon.com.br/s?k={termo_de_pesquisa.replace(' ', '+')}"
    # numero_total_paginas = paginas.obter_numero_total_paginas(
    #     url_pesquisa)
    #
    # if numero_total_paginas:
    #     print(f"Encontramos {numero_total_paginas} páginas de resultados.")
    #
    #     # Obter lista de URLs de todas as páginas
    #     lista_urls_paginas = paginas.obter_lista_urls_paginas(
    #         url_pesquisa, numero_total_paginas)
    #     for i, url_paina in enumerate(lista_urls_paginas, 1):
    #         print(f"Url da página {i}: {url_paina}")
    # else:
    #     print("Não foi possível obter o número total de páginas.")


if __name__ == "__main__":
    run()
    rodando_checkagem_de_precos()

