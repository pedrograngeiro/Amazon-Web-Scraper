# Amazon Web Scraper

Este projeto é um web scraping que coleta informações de preços de produtos relacionados ao termo de pesquisa "monitor" na Amazon. O script busca os preços dos produtos em várias páginas de resultados de busca e armazena os dados em um arquivo CSV chamado "AmazonWebScraping.csv". O projeto utiliza Python, juntamente com as bibliotecas BeautifulSoup e Requests, para extrair os dados de forma automatizada.

O objetivo é permitir que os usuários obtenham informações sobre os preços dos produtos na Amazon de forma rápida e eficiente, facilitando a comparação de preços e a identificação de boas ofertas.
Funcionalidades Principais:

    Coleta de preços de produtos relacionados ao termo "monitor" na Amazon.
    Navegação em várias páginas de resultados de busca para obter mais dados.
    Armazenamento dos dados coletados em um arquivo CSV para fácil análise e referência.

Este projeto é útil para quem deseja acompanhar os preços de produtos na Amazon ou realizar análises de preços para tomada de decisões de compra. É uma ferramenta simples e poderosa para obter informações atualizadas sobre produtos disponíveis na plataforma da Amazon.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas necessárias: `beautifulsoup4`, `requests`

## Instalação

Clone o repositório para o seu computador:

```bash
git clone https://gitlab.com/pedrograngeiro/amazon-web-scraper.git
```
```bash
git clone https://github.com/pedrograngeiro/Amazon-Web-Scraper.git
```
<br>
Navegue até o diretório do projeto:
```bash
cd Amazon-Web-Scraper
```
<br>
Instale as bibliotecas nessarias descritas em requirements.txt
```bash
pip install -r requirements.txt
```
<br>

Estrutura do Projeto
```markdown
|- main.py
|- util/
   |- precos.py
   |- paginas.py
   |- gerar_csv.py
   |- extrator.py
```

## Descrição das Funções Principais

- `main.py`: Script principal que executa a verificação de preços de produtos na Amazon.
- `util.precos`: Módulo que contém a função `check_price(url)` para coletar informações de preços de produtos da Amazon.
- `util.paginas`: Módulo que contém funções para obter o número total de páginas de resultados de busca da Amazon e navegar entre as páginas.
- `util.gerar_csv`: Módulo que contém funções para criar e atualizar um arquivo CSV chamado "AmazonWebScraping.csv" com os dados coletados.
- `util.extrator`: Módulo que contém funções auxiliares para extrair texto de elementos HTML.

## Navegação entre Páginas

- `obter_numero_total_paginas(url, print_info=False)`: Obtém o número total de páginas de resultados de busca da Amazon a partir da URL fornecida.
- `navegar_entre_paginas(url, numero_pagina, print_info=False)`: Constrói e retorna a URL de uma página específica de resultados de busca da Amazon.
- `obter_lista_urls_paginas(url, numero_total_paginas, print_info=False)`: Gera uma lista de URLs de todas as páginas de resultados de busca da Amazon, navegando de página em página.
