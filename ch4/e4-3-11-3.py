#e4-3-11-3
Ls = [["Apple",85],["Ball",74],["Car",92],["Donkey",88],[ "Horse",63]]
Ls.sort(key= lambda  x:x[],reverse = True)
print(Ls)
for i in range( 0,len( Ls) ) :
    print(Ls[ i][ 0],end = ' ')

