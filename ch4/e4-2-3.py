#e4-2-3
d= input('請輸入一個華氏溫度:')
if float(d) <= -459.67:
    print("輸入錯誤" )
else:
    print("攝氏溫度是:" )
    print(round( (float( d) - 32) /1.8,2))



