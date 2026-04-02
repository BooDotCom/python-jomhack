#io manipulation and validation

name = input("What is your name?: ")
height = input("What is your height in cm?: ")

#validate age input
while True:
    try:
        age = int(input("What is your age?: "))
        if age >= 0:
            break
        else:
            print("Age cannot be negative. Please enter a valid age.")
    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")

#output the collected information
print(f"Name: {name}")
print(f"Height: {height} cm")
print(f"Age: {age} years")