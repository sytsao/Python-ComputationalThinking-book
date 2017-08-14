#e4-3-13
for i in range( 1,11):
    s =""
    for  j in range(0,10-i):
        s += " "
    for  j in range(0,2*i-1):
        s   +="*"
    print(s)

