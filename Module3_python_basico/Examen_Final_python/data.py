#Modulo para guardar datos 

import actions
import csv


def write_data_in_CSV(file_path, students_list): #students_list va a guardar list_dic de actions.
    headers = [ 'student_name', 'student_section', 'spanish_note', 'english_note', 'scient_note', 'social_note']


    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(students_list)




def import_CSV_file(file_path, list_dic):
    try:

        list_dic.clear() #limpia la lista para que cada vez que se importa este vacia

        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:

                student = {
                    'student_name': row['student_name'],
                    'student_section': row['student_section'],
                    'spanish_note': int(row['spanish_note']),
                    'english_note': int(row['english_note']),
                    'scient_note': int(row['scient_note']),
                    'social_note': int(row['social_note'])
                }

                list_dic.append(student)

    except FileNotFoundError:
        print("No exported file found.")

