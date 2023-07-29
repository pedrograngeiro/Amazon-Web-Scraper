import time
from util.precos import check_price
from util import paginas
from util.paginas import obter_lista_urls_paginas
from util.paginas import obter_numero_total_paginas

def rodando_checkagem_de_precos():
    termo_de_pesquisa = "monitor"
    url_pesquisa = f"https://www.amazon.com.br/s?k={termo_de_pesquisa.replace(' ', '+')}"

    total_paginas = obter_numero_total_paginas(url_pesquisa)
    numero_da_pagina = paginas.obter_lista_urls_paginas(url_pesquisa, total_paginas, print_info=False)

    for url in numero_da_pagina:
        check_price(url)



if __name__ == "__main__":
    rodando_checkagem_de_precos()

