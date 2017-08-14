#e6-3-7: 上網路抓取開放資料進行處理樣本資料做常態分配檢定
import pandas as pd
import scipy.stats as stats
df1 = pd.read_csv('2017pig.csv',encoding="utf-8", sep=",")
df1.columns = [ 'total_amt', 'average_weight', 'average_price']
data=df1.describe()
s1=[]
s2=[]
s3=[]
for i in range(0, len(data.columns)):
    s=df1[df1.columns[i]]
    [s, pv1]=stats.normaltest(s)
    pv2=stats.skew(s)
    pv3=stats.kurtosis(s)    
    s1.append(pv1)
    s2.append(pv2) 
    s3.append(pv3)  
#將三個新統計量加入到df2,再與data合併     
df2 = pd.DataFrame([list(s1), list(s2), list(s3)], index=['norm','skew', 'kurt'], columns = ['total_amt', 'average_weight', 'average_price'])
df3=pd.concat([data,df2])
print(df3.round(2))
