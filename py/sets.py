#there are four data structures in python:
#list, tuple, dictionary and set

#sets are unordered collections of unique elements
#set is created using curly braces {}
#sets do not allow duplicate elements
#sets are mutable, meaning you can add or remove elements from a set after it has been created

#creating a set

drinks = {"coke", "pepsi", "sprite", "fanta"}
num1 = {1, 2, 3, 4, 5.3, 6.7}
num2 = {1, 2, 3, 4, 5.3, 6.7, 7.8}

#set operations

# drinks.add("mountain dew") #add an element to the set
# drinks.remove("coke") #remove an element from the set
# drinks.discard("pepsi") #remove an element from the set, but does not raise an error if the element is not found
# drinks.clear() #remove all elements from the set

print(drinks)

#set math operations

print(num1.union(num2)) #returns a new set that contains all the elements from both sets
print(num1.intersection(num2)) #returns a new set that contains only the elements that are common to both sets
print(num1.difference(num2)) #returns a new set that contains only the elements that are in the first set but not in the second set
print(num1.symmetric_difference(num2)) #returns a new set that contains only the elements that are in either set, but not in both sets