#4-4-2
mystr = "0122202341020303" 
print( mystr + "\n")
li = list(mystr)
for i in range(1,len(li) ,2) :
    li[ i] = '–'
mystr = "".join(li)
print( mystr)
