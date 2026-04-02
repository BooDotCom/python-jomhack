import time

while True:
    x = input("Enter the first number: ")
    try:
        x = int(x)
        if type(x) == int:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    y = input("Enter the second number: ")
    try:
        y = int(y)
        if type(y) == int:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    operand = input("""Enter the operation: 
+ for addition
- for subtraction
* for multiplication
/ for division
Your choice: """)

    if operand in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operation. Please enter a valid operation.")
        time.sleep(0.5)

if operand == '+':
    result = x + y
elif operand == '-':
    result = x - y
elif operand == '*':
    result = x * y
elif operand == '/':
    if y != 0:
        result = x / y
    else:
        result = "Error: Division by zero is not allowed."

print(f"The result of {x} {operand} {y} is: {result}")