import time
from util.precos import check_price

while True:
    url = "https://www.amazon.com.br/Monitor-AOC-G-Sync-Compatible-27G2/dp/B088L3TM7X/ref=sr_1_1?pf_rd_i=16364756011&pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_p=3a4566d3-19f5-4330-ba47-df1b7bbd88a2&pf_rd_r=TBJX7096TP23B8K7MYV4&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1689553216&s=computers&sr=1-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
    check_price(url)
    time.sleep(20)

df = pd.read_csv("AmazonWebScraping.csv")

print(df)

termo_de_pesquisa = "fone"
url_pesquisa = f"https://www.amazon.com.br/s?k={termo_de_pesquisa.replace(' ', '+')}"
print(url_pesquisa)
numero_total_paginas = paginas.obter_numero_total_paginas('https://www.amazon.com.br/s?rh=n%3A16339926011&fs=true&ref=lp_16339926011_sar')

if numero_total_paginas:
    print(f"Encontramos {numero_total_paginas} páginas de resultados.")
else:
    print("Não foi possível obter o número total de páginas.")
