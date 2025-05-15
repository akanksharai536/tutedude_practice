student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name} scored {student_marks[name]} marks.")
else:
    print("Student not found in the record.")