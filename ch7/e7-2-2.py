#e7-2-2 定義BankAccount類別
class BankAccount:
    type = '正常' 
    def __init__(self, name):
        self.userName = name
        self.balance = 0.0
    def showBalance(self): 
        print(self.balance)
    def withdrawMoney(self, amount): #提款
        self.balance -= amount
    def depositMoney(self, amount): #存款
        self.balance += amount
object1 = BankAccount("100001") 
object2 = BankAccount("100002") 
print(object1.userName)
print(object2.userName)
object1.depositMoney(100)
object2.depositMoney(200)
print(object1.balance)
print(object2.balance)
object1.showBalance()
object2.showBalance()
print(object1.type)
print(object2.type)
