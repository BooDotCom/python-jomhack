# #class: a template of creating an object. can have methods(functions)
# #objects: instance of classes

# #basic class definition

# class Person:
#     #class attribute (shared by all instances)
#     species = "Homo sapiens"

#     #constructor
#     def __init__(self,name,age):
#         #instance attributes
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"Hi I am {self.name} and I am {self.age} years old."
    
#     #Method with parameters
#     def have_birthday(self):
#         self.age +=1
#         return f"Happy bday. {self.name} is now {self.age}"
    
# #Creating objects
# person1 = Person("Abu", 60)
# person2 = Person("Ali", 50)

# #Accessing attributes
# print(person1.name)
# print(person2.age)

# #calling methods
# print(person1.introduce())
# print(person2.have_birthday())

# #Class attributes
# print(Person.species)
# print(person1.species)

class BankAccount:
    def __init__(self,account_number,owner,balance =0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            self.transaction_history.append(f"Deposited RM{amount}")
            return f"Deposited RM{amount}. New balance: RM{self.balance}"
        else:
            return "Invalid deposit amount"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -=amount
            self.transaction_history.append(f"Withdrew RM{amount}")
            return f"Withdrew RM{amount}. New balance: RM{self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
        
    def get_balance(self):
        return f"Current balance: RM{self.balance}"
    
    def get_transaction_history(self):
        return self.transaction_history

#using BankAccount class 
account = BankAccount("19239","Bob", 1000)
print(account.deposit(250))
print(account.withdraw(500))
print(account.get_balance())
