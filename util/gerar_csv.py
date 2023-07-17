import csv
import datetime

def write_to_csv(title, price):
    today = datetime.date.today()
    header = ["Title", "Price", "Date"]
    data = [title, price, today]

    # Create a csv file
    with open("AmazonWebScraping.csv", "w", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

def append_to_csv(title, price):
    today = datetime.date.today()
    data = [title, price, today]

    # Create a csv file
    with open("AmazonWebScraping.csv", "a+", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)