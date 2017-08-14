#e7-2-1  定義Dog 類別
class Dog: 
    number = 0
    def __init__(self ,name,color): 
        self.name= name  
        self.color = color 
        Dog.number = Dog.number + 1
    def bark( self) : 
        print("汪!汪!汪!我是" + self.name+ " ! ")
        print("現在有%d 條狗!"%Dog.number) 
dog1 = Dog("大黃","黃色")
print("剛才建立了一個狗物件，該條狗名叫: "+ dog1.name + "顏色為: "+ dog1.color)
dog1.bark()
dog2 = Dog("小白","白色" )
print("剛才建立了一個狗物件，該條狗名叫: "+ dog2.name + " 顏色為: "+ dog2.color)
dog2.bark()
dog1.bark()
