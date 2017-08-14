#e6-3-1: 上網路抓取股價資料
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance 
#下載資料起始日與股票代號
start="2017-01-01"
end="2017-04-30"
df = web.get_data_yahoo('2317.tw',start,end)
#日股價資料寫入excel檔
writer=pd.ExcelWriter('stock2317.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
