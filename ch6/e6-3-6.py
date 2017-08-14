#e6-3-6: 上網路抓取股價資料K 線與移動平均線
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance
import numpy as np
start = "2017-01-01"
end = "2017-07-15"
apple = web.get_data_yahoo("AAPL", start, end)
pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots
apple["5d"] = np.round(apple["Close"].rolling(window = 5, center = False).mean(), 2)
apple["20d"] = np.round(apple["Close"].rolling(window = 20, center = False).mean(), 2)
apple["50d"] = np.round(apple["Close"].rolling(window = 50, center = False).mean(), 2)
pandas_candlestick_ohlc(apple.loc[start: end,:], otherseries = ["5d","20d","50d"])
