# Student Grades using Dictionary

students = {}

while True:
    print("\nOptions:")
    print("1. Add new student")
    print("2. Update student grade")
    print("3. Print all students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added with grade {grade}")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}")
        else:
            print("Student not found.")

    elif choice == 3:
        print("\nAll Student Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
