# Task 4: Student Management System

# Store student details in a list
students = []

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "Name": name,
        "Roll Number": roll_no,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")

# Function to display all students
def display_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print("Name:", student["Name"])
            print("Roll Number:", student["Roll Number"])
            print("Marks:", student["Marks"])
            print("--------------------")

# Main menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            add_student()
        except ValueError:
            print("Error: Marks must be a valid number.")

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")