name = "Dave" # String
age = 42 # Integer
decimal = 3.14 # Float
am_single = True # Boolean

print(name)
print(type(name))
print(age)
print(type(age))
print(decimal)
print(type(decimal))
print(am_single)
print(type(am_single))

#Math operations

x= 20
y = 10

print(x+y) # Addition
print(x-y) # Subtraction
print(x*y) # Multiplication
print(x/y) # Division
print(x//y) # Floor Division
print(x%y) # Modulus
print(x**y) # Exponentiation

#celsius conversion

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)