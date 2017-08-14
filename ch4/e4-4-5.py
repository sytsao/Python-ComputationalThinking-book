#e4-4-5
while True:
    mystr = input("請輸入一個產品編碼 (quit 退出)\n" )
    if(mystr == "quit") :
        break 
    else:
        if  mystr[0] == "1":
            print("商品已上市," )
        else:
            print("商品未上市," ) 
        myyear= mystr[2:6] +"年" 
        mymonth = mystr[ 6 : 8] + "月" 
        myday = mystr[ 8:10] + "日"
        print("商品的出廠日期是"+ myyear + mymonth + myday)
