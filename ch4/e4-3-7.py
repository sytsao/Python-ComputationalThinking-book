#e4-3-7
mystr  = input("請輸入一個字串:\n")
patten_str = "0123456789" 
founderr = False
for c in mystr:
    if c not  in patten_str:
        founderr = True 
if founderr:
    print("該字串包含非數字字元")
else:
    print("該字串全是數字字元")


