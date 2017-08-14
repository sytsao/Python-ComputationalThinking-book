#e6-2-6 文字檔讀取與寫入：台積電存股規劃
import math
with open('data5.txt', 'r') as fin: 
    with open('data5_w.txt', 'w') as fout:
        for line in fin:
            data=math.ceil(20/(float(line)*0.001425))
            print('每股價格:%5.2f, 每日需購股數:%5.0f' %(float(line), data))  
            fout.write(str(data)+'\n')
