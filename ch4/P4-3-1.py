# P4-3-1敘述統計(math函式庫)
import math
sample= [5, 8, 9, 6, 4, 1, 2, 3, 5, 6]
n=len(sample)
mean=sum(sample)/n
sumi=0
for i in range(0, n):
    sumi=sumi+((sample[i]-mean)**2)
var=sumi/(n-1)    
std=math.sqrt(var)
print('樣本= ', sample)
print('平均數= ', mean)
print('最大值= ', max(sample))
print('最小值 = ', min(sample))
print('變異數= ', round(var,2))
print('標準差= ', round(std,2))
