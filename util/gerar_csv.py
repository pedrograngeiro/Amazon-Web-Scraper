import csv
import datetime

def write_to_csv(header):
    with open("AmazonWebScraping.csv", "w", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

def append_to_csv(title, price):
    today = datetime.date.today()
    data = [title, price, today]

    with open("AmazonWebScraping.csv", "a+", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)