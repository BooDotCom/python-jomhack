#dictionaries are used to store data in key and value pair.
#key must be unique, but values can have duplicates.

# student = {
#     "name:": "Bob",
#     "age:": 25,
#     "subjects:": ["French", "Geography", "History"]
# }

#accessing and modifying values of dictionary
# print(student["name:"]) #accessing value of key "name" in studdent dictionary. Result: Bob
# print(student.get("age:")) #same thing but slightly longer
# print(student["subjects:"][1])
# student["age:"] = 21 #Modifying value
# student["grade:"] = "A" #adding new value key-value

#Testing after adding/modifying
# print(student["grade:"])
# print(student["age:"])

#dictionary methods
# print(student.keys()) #return all keys
# print(student.values()) #return all values
# print(student.items()) # return key-value pairs

#Iterating dictionaries
# for key in student:
#     print(f"{key} {student[key]}\n")

# for key, value in student.items():
    # print(f"{key} {value}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#nested dictionaries

company = {
    "employees": {
        "john": {
            "age": 30,
            "department": "IT",
            "hobby": ["cooking", "reading"]
        },
        "jane": {
            "age": 25,
            "department": "HR",
            "hobby": ["shopping", "cooking"]
        }
    },
    "departments": ["IT", "HR", "Finance"]
}

# print(company["employees"]) #prints the entire employees dictionary
# print(company["employees"]["john"]) #prints the entire john dictionary
# print(company["employees"]["john"]["age"]) #prints the age key's value from john dictionary
# print(company["employees"]["john"]["hobby"][1]) #prints index 1 of "hobby" key's value from john dictionary

#modifying a nested dictionary's key-value pair
# company["employees"]["john"]["age"] = 40
# print(company["employees"]["john"]["age"])

# print(company["departments"])