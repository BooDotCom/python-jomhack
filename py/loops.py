for i in range(5): #0,1,2,3,4
    print(i)

print("-------------------")
for i in range(1,6): #1,2,3,4,5
    print(i)

print("-------------------")
for i in range(1,10,2): #1,3,5,7,9
    print(i)

print("-------------------")
print("While loop:")
count = 0
while count < 5:
    print(count)
    count += 1

print("-------------------")
print("Loop control statements:")
for i in range(10):
    if i == 3:
        continue #skip this iteration and move to the next one
    if i == 5:
        break #exit loop
    print(i)

print("-------------------")
print("Nested loops:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")