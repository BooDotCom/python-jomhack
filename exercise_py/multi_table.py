while True:
    try:
        num = int(input("Enter number: "))
        if type(num) == int:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Multiplication table for {num}:")
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")