#e6-2-5分析班級電腦課程期末考試情況
f= open("score.txt")
a = f.read()
L = a.split( )
for i in range(0,len(L)) : 
    L[ i] = int(L[ i])
#分類統計各級別人數到列表 c
c=  [0,0,0,0,0,0]
for x in L:
    if x>=90:
        c[0]+=1 
    elif  x>= 80:
        c[1] += 1
    elif  x>= 70:
        c[2] += 1 
    elif  x>= 60:
        c[3]+=1 
    elif  x>= 40:
        c[4] += 1
    else:
        c[5] += 1
#輸出各級別統計結果
print("90 分以上%d 人"%c[ 0 ],end = ',') 
print("89-80 分%d 人"%c[1],end=  ',') 
print( "79-70 分%d 人" %c[ 2],end = ',') 
print("69-60 分%d 人"%c[3],end= ',') 
print("59-40 分%d 人"%c[4 ],end= ',')
print("40 分以下%d 人"%c[5 ],end=  '\n')
