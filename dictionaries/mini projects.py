students = {}
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input("\nEnter student name: ")
    subjects = {}
    num_subjects = int(input("How many subjects? "))

    for j in range(num_subjects):
        subject = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        subjects[subject] = marks

    students[name] = subjects

print("\nStudent Dictionary:", students)
