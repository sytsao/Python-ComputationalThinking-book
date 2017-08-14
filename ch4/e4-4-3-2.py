#4-4-3-2
while True:
    str= input("請輸入一個字串(quit 退出)\n")
    if( str == "quit") :
        break
    else:
        for i in range(1,len(str)):
            if str.count('C')!= 0:
                print("找到字元C")
            else:
                print( "沒找到字元C")
