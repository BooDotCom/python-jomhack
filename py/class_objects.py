#class: a template of creating an object. can have methods(functions)
#objects: instance of classes

#basic class definition

class Person:
    #class attribute (shared by all instances)
    species = "Homo sapiens"

    #constructor
    def __init__(self,name,age):
        #instance attributes
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi I am {self.name} and I am {self.age} years old."
    
    #Method with parameters
    def have_birthday(self):
        self.age +=1
        return f"Happy bday. {self.name} is now {self.age}"
    
#Creating objects
person1 = Person("Abu", 60)
person2 = Person("Ali", 50)

#Accessing attributes
print(person1.name)
print(person2.age)

#calling methods
print(person1.introduce())
print(person2.have_birthday())

#Class attributes
print(Person.species)
print(person1.species)