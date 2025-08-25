import os
import requests
import schedule
import time

# API BTC price (contoh pakai Coindesk)
URL = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

def send_notification():
    try:
        response = requests.get(URL).json()
        price = response["bpi"]["USD"]["rate"]
        print(f"BTC Price: ${price}")
        # Kalau mau kirim ke Telegram / Discord / Email tinggal tambahin di sini
    except Exception as e:
        print(f"Error: {e}")

# Scheduler (jalan tiap jam sekali)
schedule.every().hour.do(send_notification)

