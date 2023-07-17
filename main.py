# import libraries util
from util import extrator
from util import gerar_csv

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd

# gerar_csv.write_to_csv(title, price)

# Read the csv file



def check_price():
    URL = "https://www.amazon.com.br/Monitor-AOC-G-Sync-Compatible-27G2/dp/B088L3TM7X/ref=sr_1_1?pf_rd_i=16364756011&pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_p=3a4566d3-19f5-4330-ba47-df1b7bbd88a2&pf_rd_r=TBJX7096TP23B8K7MYV4&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1689553216&s=computers&sr=1-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"

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



while True:
    check_price()
    time.sleep(60 * 60 * 24)

df = pd.read_csv("AmazonWebScraping.csv")

print(df)