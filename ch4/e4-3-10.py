#e4-3-10
monthdays  =  dict(  Jan  = 31 ,Feb = 28 ,Mar = 31,Apr = 30 ,May = 31,Jun = 30 ,Jul = 31 ,Aug=31,Sep=30,Oct=31,Nov= 30 ,Dec= 31  )
print(monthdays.keys()) #顯示字典 monthdays 的鍵值序列
print(monthdays.values()) #顯示字典 monthdays 的值序列
for i in monthdays. keys() :
    print( i,end =" ")
print(monthdays.items())	#顯示字典 monthdays 的鍵值對序列
x= {'a1' :21,'a2':34}#建立一個新的字典 x
print(x)
monthdays.update(x) #將字典 x 的鍵值對追加到字典 monthdays 中
print(monthdays)
monthdays. pop(  'a1') #刪除鍵為 'a1'的鍵值對
print(monthdays)
print(monthdays. get( 'a2')) #獲取鍵'a2'對應的值
print(monthdays. get( 'a1','not found'))	#獲取鍵'a1'對應的值，沒有找到則返回 'not found'
