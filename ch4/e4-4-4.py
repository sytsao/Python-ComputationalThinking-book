#4-4-4
while True:
    sum= 0
    str = input("請輸入一個字串(quit 退出)\n ")
    if(str == "quit"):
        break
    else:
        for i in range(1,len(str)):
            sum= sum+ int(str[i])
        if sum== int(str[0]):
            print( "找到了")
        else:
            print("找不到")
