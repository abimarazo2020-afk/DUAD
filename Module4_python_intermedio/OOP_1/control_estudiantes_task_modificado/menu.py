#Menu de opciones

import data
import actions

def show_menu(list_dic):
    while True:

        print("\n----- STUDENT SYSTEM MENU -----")
        print("1. Add student")
        print("2. Show all students")
        print("3. Get student average")
        print("4. Get top 3 students")
        print("5. Get general average")
        print("6. Show failed students")
        print("7. Delete student")
        print("8. Export student data")
        print("9. Import student")
        print("10. Exit")

        try:
            option = int(input("Choose an option (1-10): "))
        except ValueError:
            print("Invalid option. Enter a number.")
            continue

        if option == 1:
            actions.student_information(list_dic)

        elif option == 2:
            actions.show_all_students(list_dic)

        elif option == 3:
            actions.get_student_average(list_dic)

        elif option == 4:
            actions.get_top_three_students(list_dic)

        elif option == 5:
            actions.get_general_average(list_dic)

        elif option == 6:
            actions.get_failed_students(list_dic)

        elif option == 7:
            actions.delete_student(list_dic)

        elif option == 8: #to export
            data.write_data_in_CSV("students.csv", list_dic)

        elif option == 9: # to import
            data.import_CSV_file("students.csv", list_dic) # se pasa la lista para llenarla
            print(list_dic[0].name)

        elif option == 10:
            print("Exiting program...")
            break

        else:
            print("Option must be between 1 and 10.")



