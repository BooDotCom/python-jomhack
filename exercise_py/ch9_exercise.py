student_records = {
    "student_001": {
        "id": "001",
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85,92,78]
    },
    "student_002": {
        "id": "002",
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90,82,95]
    }
}

student_records["student_003"] ={
    "id": "003",
    "name": "Mike",
    "age": 20,
    "major": "Math",
    "grades": [82,79,91]
}

for key,info in student_records.items():
#     print(f"""
# Student ID: {student_records[key]["id"]}
# Name: {student_records[key]["name"]}
# Age: {student_records[key]["age"]}
# Major: {student_records[key]["major"]}
# Grades: {student_records[key]["grades"]}""")
    print(f"""
Student ID: {[info]["id"]}
Name: {[info]["name"]}
Age: {[info]["age"]}
Major: {[info]["major"]}
Grades: {[info]["grades"]}""")