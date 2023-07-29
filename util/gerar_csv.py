import csv
import datetime

def write_to_csv(header):
    """
    Cria um novo arquivo CSV chamado "AmazonWebScraping.csv" e escreve o cabeçalho fornecido.

    :param header: Lista contendo os nomes das colunas do arquivo CSV.
    :return: Nenhum valor de retorno direto.

    Notas:
    - O arquivo "AmazonWebScraping.csv" será criado na pasta atual.
    - Se o arquivo já existir, seu conteúdo será sobrescrito.
    - Certifique-se de que a lista 'header' esteja em conformidade com os dados que serão adicionados posteriormente.

    """
    with open("AmazonWebScraping.csv", "w", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

def append_to_csv(title, price):
    """
    Adiciona uma nova linha ao arquivo "AmazonWebScraping.csv" com o título, preço e data fornecidos.

    :param title: O título do produto a ser adicionado.
    :param price: O preço do produto a ser adicionado.
    :return: Nenhum valor de retorno direto.

    Notas:
    - A data atual será adicionada automaticamente na coluna 'Date'.
    - Certifique-se de que os dados fornecidos estejam em conformidade com o cabeçalho do arquivo CSV.

    """

    today = datetime.date.today()
    data = [title, price, today]

    with open("AmazonWebScraping.csv", "a+", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)