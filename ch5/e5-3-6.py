#e5-3-6猜數字遊戲
import  random
def  echo(guess_number,x) :
    if x>guess_number:
        return 1
    elif x < guess_number :
        return -1 
    else:
        return 0
gn = random.randint( 1,1000)
count  = 1
while count <= 10:
    x = int( input("請猜數(第%d 次)"%count) )
    check= echo( gn,x)
    if check == 0:
        break
    elif check > 0 :
        print("猜大了!" )
    else:
        print("猜小了!" )
    count  += 1 
if count> 10:
    print( "遊戲結束,你失敗了.")
else:
    print(" 恭喜你猜對了,共猜了%d 次"%count)
