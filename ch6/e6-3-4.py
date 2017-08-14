#e6-3-4: 上網抓取股價資料畫折線圖
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance 
start ="2017-01-01"
end = "2017-07-15"
data = web.get_data_yahoo("AAPL", start, end)
# This line is necessary for the plot to appear in a Jupyter notebook
%matplotlib inline 
# Control the default size of figures in this Jupyter notebook
%pylab inline
pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots
data["Adj Close"].plot(grid = True) # Plot the adjusted closing price of AAPL
