while True:
    weight = input("Enter your weight in kg: ")
    try:
        weight = float(weight)
        if weight > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a valid weight.")

while True:
    height = input("Enter your height in meters: ")
    try:
        height = float(height)
        if height > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a valid height.")

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 24.9 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")