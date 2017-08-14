#e4-3-5
x = 10000#本金 10000 元
years=0
while x < 20000 :
    years += 1
    x = x* (1+0.019)
print(str(years) +"年以後，存款會增加1倍")
