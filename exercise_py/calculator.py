x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
operand = input("""Enter the operation: 
+ for addition
- for subtraction
* for multiplication
/ for division
Your choice: """)

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