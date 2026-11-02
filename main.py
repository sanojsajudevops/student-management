students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("-------------------")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Course:", student["course"])

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
