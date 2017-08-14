#e6-3-3: 上網路抓取股價資料畫高低圖
import pandas as pd
from pandas_datareader import data as web
import fix_yahoo_finance 
#下載資料起始日與股票代號
start="2017-01-01"
end="2017-04-30"
df = web.get_data_yahoo('2317.tw',start,end)
#日股價資料寫入excel檔
writer=pd.ExcelWriter('2317.xlsx')
df.to_excel(writer,'2317')
workbook = writer.book
worksheet = writer.sheets['2317']
#畫高低圖
chart = workbook.add_chart({'type': 'stock'})
chart.add_series({'name': '=2317!$B$1','categories': '=2317!$A$2:$A$14','values': '=2317!$B$2:$B$14'})
chart.add_series({'name': '=2317!$C$1','categories': '=2317!$A$2:$A$14','values': '=2317!$C$2:$C$14'})
chart.add_series({'name': '=2317!$D$1','categories': '=2317!$A$2:$A$14','values': '=2317!$D$2:$D$14'})
chart.set_title ({'name': 'High-Low-Close'})
chart.set_x_axis({'name': 'Date'})
chart.set_y_axis({'name': 'Share price'})
worksheet.insert_chart('I2', chart)
writer.save()
