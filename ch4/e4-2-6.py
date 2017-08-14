#e4-2-6
print("輸入 1 完成華氏轉攝氏溫度\n") 
print("輸入 2 完成攝氏溫度轉華氏\n" ) 
opt = input ("請輸入 1 or 2:")
if opt ==  '1':
    d= input('請輸入華氏溫度: ')
    if float( d)  <=  - 459.67 :
        print("輸入錯誤" )
    else:
        print("轉換的攝氏溫度是:")
        print(round( (float(d)  - 32)/1.8,2))
elif  opt ==  '2':
    d = input('請輸入攝氏度: ')
    if float(d)<= -273.15:
        print("輸入錯誤" )
    else: 
        print("轉換的華氏溫度是:")
        print(round((float(d)*1.8)+32,2))
else:
        print("輸入錯誤")
