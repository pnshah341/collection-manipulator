# Student Data Organizer
# Practical 3: Collection Manipulator

students = []
student_details= {}
subjects = set()

print("="*90)
print("   WELCOME TO STUDENT DATA ORAGANIZER")
print("="*90)




while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")


        if sid in student_details:
            print("Student ID already exists!")

        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth: ")

            sub = input("Enter Subjects (comma separated): ")
            sub = sub.split(",")

            for i in range(len(sub)):
                sub[i] = sub[i].strip().title()

            info = (sid, dob)

            student = {
                "Name": name,
                "Age": age,
                "Grade": grade,
                "Subjects": sub,
                "Info": info
            }

            students.append(student)
            student_details[sid] = student

            for s in sub:
                subjects.add(s)

            print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")

        else:
            for sid, student in student_details.items():
                print("\nStudent ID:", sid)
                print("Name: {}".format(student["Name"]))
                print("Age: %d" % student["Age"])
                print(f"Grade: {student['Grade']}")
                print("DOB:", student["Info"][1])
                print("Subjects:", student["Subjects"])

    elif choice == "3":
        sid = input("Enter Student ID: ")

        if sid in student_details:
            print("1. Update Age")
            print("2. Update Grade")

            ch = input("Enter choice: ")

            if ch == "1":
                age = int(input("Enter new age: "))
                student_details[sid]["Age"] = age
                print("Age updated successfully!")

            elif ch == "2":
                grade = input("Enter new grade: ")
                student_details[sid]["Grade"] = grade
                print("Grade updated successfully!")

            else:
                print("Invalid choice!")

        else:
            print("Student not found!")

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")

        if sid in student_details:
            student = student_details[sid]
            students.remove(student)
            del student_details[sid]

            subjects = set()

            for s in students:
                for sub in s["Subjects"]:
                    subjects.add(sub)

            print("Student deleted successfully!")

        else:
            print("Student not found!")

    elif choice == "5":
        print("Unique Subjects Offered:")

        for s in subjects:
            print(s)

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice!")
