#print("hello world")

while True:
    x = input("Enter the first number: ")
    try:
        x = int(x)
        if type(x) == int:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")