class BankAccount :
    def __init__(self, name, balance):
        self._name=name     #protected
        self.__balance= balance     #private

    def get_balance(self) :     #getter
        return self.__balance 
    
    def set_balance(self, newBalance) :
        self.__balance=newBalance

acc1 = BankAccount("abc", 20000)
acc1.set_balance(400000)
print(acc1._name, acc1.get_balance())