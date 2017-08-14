#e6-3-5: 上網路抓取股價資料畫K線圖
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance 
import matplotlib.dates as mdates
import matplotlib.pyplot as plt   # Import matplotlib
from matplotlib.finance import candlestick_ohlc
start = "2017-01-01"
end = "2017-07-15"
data = web.get_data_yahoo("AAPL", start, end)
data = data.reset_index()
data['Date2'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
tuples = [tuple(x) for x in data[['Date2','Open','High','Low','Close']].values]
pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots
fig, ax = plt.subplots()
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("AAPL")
candlestick_ohlc(ax, tuples, width=.6, colorup='g', alpha =.4)
