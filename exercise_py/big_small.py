# num_list = [-10, 0, 5, 3.14, 100, -2.718]

num_list = []
while True:
    try:
        input_value = input("Enter a number to add to list. Enter done when finished: ")
        if input_value.lower() == "done":
            break
        num_list.append(float(input_value))
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

#find the biggest and smallest number in using min() and max()
# biggest = max(num_list)
# smallest = min(num_list)

#finding the biggest and smallest number using a for loop
biggest = num_list[0]
smallest = num_list[0]

for i in num_list:
    if i > biggest:
        biggest = i
    if i < smallest:
        smallest = i

#max(): returns the largest item in an iterable or the largest of two or more arguments.
#min(): returns the smallest item in an iterable or the smallest of two or more arguments.  

print("The biggest number is: ", biggest)
print("The smallest number is: ", smallest)