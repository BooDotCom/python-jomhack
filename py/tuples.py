birthday = (1990, 5, 17)

print("Day of birth: ", birthday[2])
print("Month of birth: ", birthday[1])
print("Year of birth: ", birthday[0])

birthday.append(12)  # This will raise an AttributeError because tuples are immutable
# birthday.reverse()  # This will also raise an AttributeError because tuples do not have a reverse method
# birthday.pop()  # This will raise an AttributeError because tuples do not have a pop method