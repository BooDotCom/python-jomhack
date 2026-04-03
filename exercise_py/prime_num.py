while True:
    try:
        num = int(input("Enter number: "))
        if num >= 0 and num <=20:
            break
        else:
            print("Please enter a number between 0 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Prime numbers until {num}:")

for i in range(2,num+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)