#e7-2-3  定義GuideDog 類別
class Dog: 
    number = 0
    def __init__(self ,name,color): 
        self.name= name  
        self.color = color 
        Dog.number += 1
    def bark( self) : 
        print("汪!汪!汪!我是" + self.name+ " ! ")
        print("現在有%d 條狗!"%Dog.number) 
class GuideDog(Dog) : 
    def __init__ (self ,name,color,year): 
        self.workyear = year#增加新屬性 workyear
        Dog. __init__  (self ,name,color) 
    def guide(self): # 
        print("我正在引導我的主人!" )
        print("我有%d 年的工作經歷! " %self.workyear)
gDog1= GuideDog("小黑","黑色",3) #建立導盲犬物件 gDogl
print("剛才建立了一個導盲犬物件，該導盲犬叫: "+ gDog1.name + " 顏色為: "+ gDog1.color+"工作經歷: "+ str(gDog1.workyear)+"年 ")
gDog1.bark()
gDog1.guide()
