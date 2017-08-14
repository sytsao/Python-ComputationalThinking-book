#e6-3-2上網路抓取股價資料
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance
import datetime
import time
starttime = time.clock()
#下載資料起始日與股票代號
start="2000-01-01"
end="2017-04-30"
writer=pd.ExcelWriter('stocprice.xlsx')
#以迴圈依公司代號順序抓取資料，並個別依公司代號命名工作表
stockid=('2303', '2330', '3008', '2498', '2311', '2409', '2357', '2317')
for i in range(0,len(stockid)):
    sid=stockid[i]+'.tw'   
    df = web.get_data_yahoo(sid, start,end)
    df.to_excel(writer,stockid[i])
#日股價資料寫入excel檔
writer.save()
endtime = time.clock()
print('程式執行時間 = %d %s' %(round(endtime - starttime), '秒'))
