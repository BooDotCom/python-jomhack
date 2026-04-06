#basic exception/error handling
#wanna know what exception does what? check reference_links.txt

# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input, please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

#using else and finally

# try:
#     file = open("test.txt", "r")
# except FileNotFoundError:
#     print("File not found")
# else:
#     #execute if no exception occured
#     content = file.read()
#     print("File read successfully)")
# finally:
#     #always executes
#     if 'file' in locals() and not file.closed:
#         file.close()
#     print("Cleanup completed")

#raisin exceptions
def validate_age(age):
    if age<0:
        raise ValueError("Age cannot be less than 0")
    if age >150:
        raise ValueError("Age is definitely real.NOT")
    
try:
    validate_age(200)
    # validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")