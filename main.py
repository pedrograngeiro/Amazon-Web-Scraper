import time
from util.precos import check_price
from util import paginas
from util.paginas import obter_lista_urls_paginas
from util.paginas import obter_numero_total_paginas

def rodando_checkagem_de_precos():
    """
        Executa a verificação de preços de produtos na Amazon.

        Esta função obtém os preços de produtos relacionados ao termo de pesquisa "monitor"
        na Amazon e armazena-os em um arquivo CSV chamado "AmazonWebScraping.csv".

        Notas:
        - Certifique-se de ter os módulos personalizados 'util.precos' e 'util.paginas' no projeto.
        - Antes de executar a função, instale as bibliotecas 'beautifulsoup4' e 'requests'.
        - Certifique-se de que o arquivo 'AmazonWebScraping.csv' seja criado na pasta do projeto.

        Exemplo de uso:
        ```
        rodando_checkagem_de_precos()
        ```

        Retorna:
        Nenhum valor de retorno.

        Autor: [Seu Nome]

        """
    termo_de_pesquisa = "monitor"
    url_pesquisa = f"https://www.amazon.com.br/s?k={termo_de_pesquisa.replace(' ', '+')}"

    total_paginas = obter_numero_total_paginas(url_pesquisa)
    numero_da_pagina = paginas.obter_lista_urls_paginas(url_pesquisa, total_paginas, print_info=False)

    for url in numero_da_pagina:
        check_price(url)



if __name__ == "__main__":
    rodando_checkagem_de_precos()

