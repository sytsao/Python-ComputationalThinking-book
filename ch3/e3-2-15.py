#e3-2-15
print(int( "123"))## int("123") 可將字串"123"轉換為整數 123
print(int(78.9)) ##  int(78.9)得到整數 78( 去掉尾部小數)
## reper( obj) ，將任意值轉為字串，常用於構造輸出字串
x  =  10  * 3.25
y  =   200   *  200
s = 'The  value of  x  is ' + repr(x)+' and  y is' + repr(y)  + '...'
print( s )
print(round(78.3456,2)) ##使用 round(x,n) 可按"四捨五入"法對 x 保留 n 位小數
print(len( "Good morning"))##使用 len(s) 計算字串的長度
