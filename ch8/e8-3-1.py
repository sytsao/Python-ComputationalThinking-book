#e8-3-1抓取台銀匯率資訊
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime, strptime, mktime
from datetime import datetime
from os.path import exists
import matplotlib.pyplot as plt
html = urlopen("http://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html, "lxml")
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    currency_name = currency_name.replace("\r","")
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0]
    print(currency_name, currency_rate)
    file_name = "e8-3-1" + currency_name + ".csv"
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
    f = open(file_name, "a")
    w = csv.writer(f)
    w.writerows(data)
    f.close()
