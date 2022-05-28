# Asynchronous
import time, requests
from openpyxl import Workbook
from openpyxl import load_workbook
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()
filename = "Crypto_Prices.xlsx"
workbook = load_workbook(filename)
worksheet = workbook.worksheets[0]

@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    response = requests.get('http://api.coincap.io/v2/assets/bitcoin')
    bitcoin_price = response.json()['data']['priceUsd']
    print('Bitcoin Price:', bitcoin_price)
    timestamp = "{}".format(time.ctime())
    bitcoin_price_row = ['Bitcoin', bitcoin_price, timestamp]
    worksheet.append(bitcoin_price_row)

@tl.job(interval=timedelta(seconds=10))
def sample_job_every_10s():
    response = requests.get('http://api.coincap.io/v2/assets/litecoin')
    litecoin_price = response.json()['data']['priceUsd']
    timestamp = "{}".format(time.ctime())
    litecoin_price_row = ['Litecoin', litecoin_price, timestamp]
    worksheet.append(litecoin_price_row)


tl.start()

while True:
  try:
    time.sleep(1)
  except KeyboardInterrupt:
    workbook.save(filename)
    tl.stop()
    break