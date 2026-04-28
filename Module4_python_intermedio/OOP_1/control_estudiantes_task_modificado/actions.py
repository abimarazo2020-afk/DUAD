'''                             MODULO DE FUNCIONES                             '''
 

from student import Student

#Funcion para pedir la informacion del estudiante
def student_information(list_dic):
    name_student = validate_student_name()
    section = validate_student_section()
        
    for student in list_dic:
        if student.name == name_student and student.section == section:
            print("Student already exists")
            return

    spanish_note = validate_notes('spanish')
    english_note = validate_notes('english')
    scient_note = validate_notes('scient')
    social_note = validate_notes('social')

    # antes era diccionario, ahora es objeto
    student = Student(
        name_student,
        section,
        spanish_note,
        scient_note,
        social_note,
        english_note
    )

    list_dic.append(student)
    print(list_dic)


#Funcion que valida el nombre del estudiante
def validate_student_name(): # cambiar agregar espacios y apellidos 
    while True:
        student_name = input('Enter your student name: ')
        if student_name.replace(" ", "").isalpha():
            return student_name
        else:
            print('The name must contain only letters')


#Funcion que valida la seccion del estudiante
def validate_student_section():
    while True:
        section = input("Enter student section (example 11B): ")

        if len(section) != 3:
            print("Section must have 3 characters")
            continue

        if not section[0:2].isdigit():
            print("First two characters must be numbers")
            continue

        if not section[2].isalpha():
            print("Last character must be a letter")
            continue

        return section.upper()

# len(section) != 3 >>>> La sección debe tener 3 caracteres
# section[:2].isdigit() >>> Los dos primeros deben ser números
# section[2].isalpha() >>>>> El tercer carácter debe ser letra
# return section.upper() esto convierte 11b → 11B


#Funcion que valida notas
def validate_notes(subject_note):
    while True:

        try:
            current_note = input(f'Enter your {subject_note} note: ')
            if 0 <= int(current_note) <= 100:
                return int(current_note) #sin el int devuelve str no un numero y ocupamos promedios
            else:
                print('The note must be between 0 and 100')
        except ValueError:
            print('This is invalid, enter a valid number: ')


#Funcion para borrar estudiante
def delete_student(list_dic):
    name_to_delete = input('Enter the student name you want to remove: ')
    section_to_delete = validate_student_section()

    for student in range(len(list_dic)):
        if list_dic[student].name == name_to_delete: # ahora es objeto
            if list_dic[student].section == section_to_delete:

                confirm = input('Are you sure you want to delete the user? (y/n): ')
                if confirm.lower() == 'y':
                    list_dic.pop(student)
                    print("Student removed")
                    print(list_dic)
                    
                return #con el return terminamos el ciclo

    print("Student not found") #si no se encuentra el student print this


#Funcion para obtener el promedio individual de cada estudiante > con parametro estudiante 
def calculate_student_average(student): # cambiar quitar math 
    spanish_note = student.spanish_note
    english_note = student.english_note
    scient_note = student.scient_note
    social_note = student.social_note

    average = (spanish_note + english_note + social_note + scient_note) / 4
    return average # para usar despues el resultado


#Funcion que busca el nombre del estudiante y llama a la funcion que saca el promedio 
def get_student_average(list_dic):
    student_name = input('Enter the student name to get the average: ')
    
    for student in list_dic:
        if student.name == student_name:

            average_result = calculate_student_average(student) #Aqui es donde llamamos a la funcion que llamar a la funcion que saca el promedio
            print(average_result)
            return

    print("Student not found")


#Funcion para generar un promedio entre todos los estudiantes 
def get_general_average(list_dic):

    if not list_dic:
        print("No students registered")
        return

    total = 0

    for student in list_dic:
        total += calculate_student_average(student)

    print(total / len(list_dic))


#Funcion para sacar el top 3 de los estudiante 
def get_top_three_students(list_dic):

    second_list = []

    for student in list_dic:

        average = calculate_student_average(student)
        student_name = student.name
        second_list.append((average, student_name)) #aqui usamos una tupla para poder pasar los dos valores
#        second_list.append((average, student["student_name"])) # si queremos evitar una variable extra.
        
    second_list.sort(reverse=True)
    top_three = second_list[:3]
    print(top_three)


#Funcion para enlistar los estudiantes reprobados
def get_failed_students(list_dic):
    
    failed_students_list = []
    

    for student in list_dic:

        #lista para materias porque pueden ser mas de una.
        subjects_list = [] #va a adentro para que con cada estudiante se reinicie la lista

        #guardamos datos del objeto en variables
        student_name = student.name
        section = student.section
        spanish_subject = student.spanish_note
        english_subject = student.english_note
        scient_subject = student.scient_note
        social_subject = student.social_note

        #comparaciones de las notas a agregar a la lista de materias
        if spanish_subject < 60:
            subjects_list.append(('spanish', spanish_subject))
        
        if english_subject < 60:
            subjects_list.append(('english', english_subject))
        
        if scient_subject < 60:
            subjects_list.append(('scient', scient_subject))
        
        if social_subject < 60:
           subjects_list.append(('social', social_subject))

        if subjects_list:
            failed_students_list.append((student_name, section, subjects_list))


    print(failed_students_list)


#funcion que muestra todos los estudiantes
def show_all_students(list_dic):

    if not list_dic:
        print("No students registered")
        return #aqui no retornaria nada > none

    for student in list_dic:
        print(student)