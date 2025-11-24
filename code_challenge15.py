import os
import json

os.system('cls')
print("──────────────────────────")
print("Student Information System")
print("──────────────────────────\n")


#empty dictionary
student_records = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - Add Student Record")
    print("B - Print all Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - Import Student Record")
    print("X - Exit System")

    choice = input("SELECT FROM THE OPTIONS ABOVE ───> ").lower()

    if choice == 'a':
        print("\n──────────────────────")
        print("Adding Student Record")
        print("──────────────────────")

        id_no = (input("Please input Student's ID Number ───> ")).upper()
        first_name = (input("Please input Student's First Name ───> ")).upper()
        last_name = (input("Please input Student's Last Name ───> ")).upper()
        age = eval(input("Please input Student's Age ───> "))
        course = (input("Please input Student's Course ───> ")).upper()
        section = (input("Please input Student's Section ───> ")).upper()

        student_records[id_no] = [first_name, last_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")

        continue

    elif choice == 'b':
        os.system('cls')
        print("───────────────────────")
        print("PRINTING STUDENT RECORD")
        print("───────────────────────")

        for i, j in student_records.items():
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
        continue

    elif choice == 'c':
        os.system('cls')

        print("─────────────────────")
        print("SEARCH STUDENT RECORD")
        print("─────────────────────")

        search_id = input("Input Student ID for search: ").lower()

        for each_id in student_records.keys():
            if search_id in student_records.keys():
                print("\n────────────────────────────")
                print("\n\nRECORD FOUND FOR ID")

                for i in student_records[search_id]:
                    print(f" ── {i}")
                print("────────────────────────────")
            else:
                print("\nNO RECORD FOUND")
            break
        continue

    elif choice == 'd':
        os.system('cls')

        print("─────────────────────")
        print("DELETE STUDENT RECORD")
        print("─────────────────────")

        search_id = input("Input Student ID for search: ").lower()

        for each_id in student_records.keys():
            if search_id in student_records.keys():
                print("\n────────────────────────────")
                print("\n\nRECORD FOUND FOR ID")

                for i in student_records[search_id]:
                    print(f" ── {i}")
                print("────────────────────────────")

                student_records.pop(search_id)
                print("\nRECORD DELETED")

            else:
                print("\nNO RECORD FOUND")
            break
        continue

    elif choice == 'e':
        os.system('cls')

        print("─────────────────────")
        print("EDIT/MODIFY STUDENT'S RECORD")
        print("─────────────────────")

        search_id = input("Input Student ID for search: ").lower()

        for each_id in student_records.keys():
            if search_id in student_records.keys():
                print("\n────────────────────────────")
                print("\n\nRECORD FOUND FOR ID")

                for i in student_records[search_id]:
                    print(f" ── {i}")
                print("────────────────────────────")

                id_no = (input("Please input Student's ID Number ───> ")).upper()
                first_name = (input("Please input Student's First Name ───> ")).upper()
                last_name = (input("Please input Student's Last Name ───> ")).upper()
                age = eval(input("Please input Student's Age ───> "))
                course = (input("Please input Student's ID Course ───> ")).upper()
                section = (input("Please input Student's Section ───> ")).upper()

                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = age
                student_records[search_id][3] = course
                student_records[search_id][4] = section

                print("\nDATA UPDATED")

            else:
                print("\nNO RECORD FOUND")
            break
        continue


    elif choice == 'f':
        os.system('cls')

        print("EXPORT STUDENT'S DATA")
        
        with open('students_records.json', 'w') as new_file:
            json.dump(student_records, new_file, indent = 4)

        print("\n\nDATA EXPORTED TO JSON")

        continue

    elif choice == 'g':
        os.system('cls')

        print("IMPORT STUDENT'S DATA")
        
        with open('students_records.json', 'r') as new_file:
            imported_records = json.load(new_file)

        student_records = imported_records
        print("\n\nDATA IMPORTED TO JSON")

        continue

    elif choice == 'x':
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE, RE-ENTER YOUR CHOICE")
        continue

        
