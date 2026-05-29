class Laptop :
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM 
        self.storage = storage

    @classmethod
    def get_storage_type(cls) :     #class method
        print(f"storage type is {cls.storage_type}")

    def get_info(self) :    #instance method
        print(f"laptop has {self.RAM} ram, {self.storage} storage and {self.storage_type} storage type")    

    @staticmethod   
    def cal_discount(price, discount) :     #static method
        final_price = price - price*(discount/100)
        print(f"final price is {final_price}")


l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.cal_discount(40000, 20)


class Products :
    count=0

    def __init__(self, name, price) :
        self.name=name
        self.price=price
        Products.count+=1

    def get_info(self) :    #instance method
        print(f"price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls) :    #class method
        print(f"total products in store : {cls.count}")

    @staticmethod   
    def cal_discount(price, discount) :     #static method
        final_price = price - price*(discount/100)
        print(f"final price is {final_price}")

p1 = Products("pen", 20)
p2 = Products("laptop", 40000)

p1.get_info()
p2.get_info()
Products.get_count()