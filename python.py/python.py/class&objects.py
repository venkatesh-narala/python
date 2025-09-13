
# class Car:
#     def __init__(self, brand):
#         self.brand = brand

# # Creating objects
# car1 = Car("supra")
# car2 = Car("merceds")
# car1.__init__("bmw")
# # print(car1.brand)  # BMW
# print(car1)
# car2.__init__("tesla")

# print(car2.brand)  # Tesla


# def display_info():
#     s="nani"
#     print( s[::-1])

# display_info()




class Car:
    def __init__(self, brand):
        self.brand = brand

# Creating objects
car1 = Car("supra")
car2 = Car("merceds")
# car1.__init__("bmw")
# print(car1.brand)  # BMW
print(car1.brand)
# car2.__init__("tesla")

print(car2.brand)  # Tesla


class car :
    def __init__(self, brand,model):
        self.brand=brand
        self.model=model
    def display_info (self):
        print(f"car : {self.brand} {self.model} ")
car1=car("toyato","corolla")
car1.display_info()


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(amount)
    def get_balance(self):  # controlled access
        return self.__balance


# Creating object
acc = BankAccount(1000)

# Accessing through method (allowed)
acc.deposit(500)
print(acc.get_balance())   # 1500
# Direct access (not allowed) → AttributeError
# print(acc.__balance)

# But Python does "name mangling"
print(acc._BankAccount__balance)  # 1500 (not recommended)
