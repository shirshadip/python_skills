# Student Grade Calculator - Full of Bugs!
# This program calculates student grades and statistics

import math

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade!")
    
    def calculate_average(self):
        if len(self.grades) == 0:  # Bug 1: Assignment instead of comparison
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

def calculate_class_statistics(students):
    total_students = len(students)
    total_grades = 0
    all_grades = []
    
    for student in students:
        if len(student.grades) > 0:
            all_grades.extend(student.grades)
            total_grades += len(student.grades)
    
    if total_grades == 0:
        return None
    
    # Bug 2: Division by zero potential
    class_average = sum(all_grades) / total_grades
    
    # Bug 3: Wrong variable name
    highest_grade = max(all_grades)
    lowest_grade = min(all_grades)
    
    return {
        'average': class_average,
        'highest': highest_grade,
        'lowest': lowest_grade,
        'total_students': total_students
    }

def read_student_data(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for line in lines:
            # Bug 4: Index error potential
            parts = line.strip().split(',')
            name = parts[0]
            age = int(parts[1])
            
            student = Student(name, age)
            
            # Bug 5: Wrong range - should start from index 2
            for i in range(1, len(parts)):
                try:
                    grade = float(parts[i])
                    student.add_grade(grade)
                except ValueError:
                    print(f"Invalid grade format for {name}: {parts[i]}")
            
            students.append(student)
    
    except FileNotFoundError:
        print("File not found!")
        return []
    
    return students

def display_student_report(student):
    print(f"\n--- Report for {student.name} ---")
    print(f"Age: {student.age}")
    print(f"Grades: {student.grades}")
    
    # Bug 6: Potential division by zero
    average = student.calculate_average()
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {student.get_letter_grade()}")
    
    # Bug 7: Logic error - always shows same message
    if len(student.grades) >= 3:
        print("Student has enough grades for evaluation")
    elif len(student.grades) >= 3:
        print("Student needs more grades")

def main():
    print("Student Grade Calculator")
    print("=" * 30)
    
    # Bug 8: Trying to access non-existent file
    students = read_student_data("students.txt")

    if not students:
        print("No students found. Creating sample data...")
        
        # Create sample students
        alice = Student("Alice", 20)
        alice.add_grade(85)
        alice.add_grade(92)
        alice.add_grade(78)
        
        bob = Student("Bob", 19)
        bob.add_grade(90)
        bob.add_grade(88)
        
        charlie = Student("Charlie", 21)
        charlie.add_grade(75)
        charlie.add_grade(82)
        charlie.add_grade(79)
        charlie.add_grade(85)
        
        students = [alice, bob, charlie]
    
    # Display individual reports
    for student in students:
        display_student_report(student)
    
    # Calculate class statistics
    print("\n" + "=" * 30)
    print("Class Statistics")
    print("=" * 30)
    
    stats = calculate_class_statistics(students)
    
    if stats:
        print(f"Class Average: {stats['average']:.2f}")
        print(f"Highest Grade: {stats['highest']}")
        print(f"Lowest Grade: {stats['lowest']}")
        print(f"Total Students: {stats['total_students']}")
    else:
        print("No grades available for statistics")
    
    # Bug 9: String concatenation type error
    print("Analysis complete for ", len(students) , " students")
    
    # Bug 10: Indentation error
    print("Thank you for using the Grade Calculator!")

# Bug 11: Missing condition
if __name__ == "__main__":
    main()