#e6-3-8 :計算技術指標-MACD/RSI
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance
import talib as ta
import numpy as np
start = "2017-01-01"
end = "2017-07-15"
df1 = web.get_data_yahoo('2317.tw',start,end)
dif,dea,macd = ta.MACD(df1["Close"].values, fastperiod=12, slowperiod=26, signalperiod=9)
df1["dif"] = dif
df1["dea"] = dea
df1["macd"] = macd
df1["rsi"] = ta.RSI(df1["Close"].values,6)
writer=pd.ExcelWriter('RSI2317.xlsx')
df1.to_excel(writer,'2317')
workbook = writer.book
worksheet = writer.sheets['2317']
writer.save()
