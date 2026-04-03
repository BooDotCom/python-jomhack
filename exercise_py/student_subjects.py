grades=[
    ("Alice", "Math", 85),
    ("Bob", "Science", 90),
    ("Alice", "Science", 92),
    ("Charlie", "Math", 78),
    ("Bob", "Math", 88),
    ("Charlie", "English", 80),
]

grades.append(("David", "French", 82)) #adding a new grade for David in French
#using sets to find unique students and subjects
students = set()
subjects = set()

for grade in grades:
    students.add(grade[0]) #add the student name to the set
    subjects.add(grade[1]) #add the subject name to the set

print("Students:")
for student in students:
    print(f" - {student}")

print("\nSubjects:")
for subject in subjects:
    print(f" - {subject}")