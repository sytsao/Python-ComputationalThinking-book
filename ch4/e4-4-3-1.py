#4-4-3-1
while True:
    str = input ( "請輸入一個字串(quit 退出 )\n")
    if(str== "quit"):
        break
    else:
        findok= False
        for mychar in str:
            if mychar=='C':
                findok = True
                break
        if findok:
            print("找到字元C")
        else:
            print("沒找到字元C")
