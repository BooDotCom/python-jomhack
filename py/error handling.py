#basic exception/error handling
#wanna know what exception does what? check reference_links.txt

try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input, please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

