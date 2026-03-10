'''                             MODULO DE FUNCIONES                             '''


#Lista de diccionarios global
list_dic = [] 


#Funcion para pedir la informacion del estudiante
def student_information():
    name_student = validate_student_name()
    section = validate_student_section()
        
    for student in list_dic:
        if student["student_name"] == name_student and student["student_section"] == section:
            print("Student already exists")
            return


    spanish_note = validate_notes('spanish')
    math_note = validate_notes('math')
    english_note = validate_notes('english')
    scient_note = validate_notes('scient')
    social_note = validate_notes('social')

    dic_student = {

        'student_name' : name_student,
        'student_section' : section,
        'spanish_note' : spanish_note,
        'math_note' : math_note,
        'english_note' : english_note,
        'scient_note' : scient_note,
        'social_note' : social_note
    }

    list_dic.append(dic_student)
    print(list_dic)


#Funcion que valida el nombre del estudiante
def validate_student_name():
    while True:
        student_name = input('Enter your student name: ')
        if student_name.isalpha():
            return student_name
        else:
            print('The name must contain only letters')





#Funcion que valida la seccion del estudiante
def validate_student_section():
    while True:
        section = input("Enter student section (example 11B): ")

        if section:
            return section

        print("Section cannot be empty")




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
def delete_student():
    deleted_user = input('Enter the student name you want to remove: ')

    for student in range(len(list_dic)):
        if list_dic[student]["student_name"] == deleted_user: #se accede a su posicion y luego al dic.
            list_dic.pop(student)
            print("Student removed")
            print(list_dic)
            return

    print("Student not found")




#Funcion para obtener el promedio individual de cada estudiante > con parametro estudiante 
def calculate_student_average(student):
    spanish_note = student["spanish_note"]
    math_note = student["math_note"]
    english_note = student["english_note"]
    scient_note = student["scient_note"]
    social_note = student["social_note"]

    average = (spanish_note + math_note + english_note + social_note + scient_note) / 5
    return average # para usar despues el resultado




#Funcion que busca el nombre del estudiante y llama a la funcion que saca el promedio 
def get_student_average():
    student_name = input('Enter the student name to get the average: ')
    
    for student in list_dic:
        if student["student_name"] == student_name:

            average_result = calculate_student_average(student) #Aqui es donde llamamos a la funcion que llamar a la funcion que saca el promedio
            print(average_result)
            return

    print("Student not found")



#Funcion para generar un promedio entre todos los estudiantes 
def get_general_average():

    if not list_dic:
        print("No students registered")
        return

    total = 0

    for student in list_dic:
        total += calculate_student_average(student)

    print(total / len(list_dic))


#Funcion para sacar el top 3 de los estudiante 
def get_top_three_students():

    second_list = []

    for student in list_dic:

        average = calculate_student_average(student)
        student_name = student["student_name"]
        second_list.append((average, student_name)) #aqui usamos una tupla para poder pasar los dos valores
#        second_list.append((average, student["student_name"])) # si queremos evitar una variable extra.
        
    second_list.sort(reverse=True)
    top_three = second_list[:3]
    print(top_three)


 

#Funcion para enlistar los estudiantes reprobados
def get_failed_students():
    
    failed_students_list = []
    

    for student in list_dic:

        #lista para materias porque pueden ser mas de una.
        subjects_list = [] #va a adentro para que con cada estudiante se reinicie la lista

        #guardamos datos del diccionario en variables
        student_name = student["student_name"]
        section = student["student_section"]
        spanish_subject = student["spanish_note"]
        english_subject = student["english_note"]
        math_subject = student["math_note"]
        scient_subject = student["scient_note"]
        social_subject = student["social_note"]

        #comparaciones de las notas a agregar a la lista de materias
        if spanish_subject <= 60:
            subjects_list.append(('spanish', spanish_subject))
        
        if english_subject <= 60:
            subjects_list.append(('english', english_subject))
        
        if math_subject <= 60:
            subjects_list.append(('math', math_subject))
        
        if scient_subject <= 60:
            subjects_list.append(('scient', scient_subject))
        
        if social_subject <= 60:
           subjects_list.append(('social', social_subject))

        if subjects_list:
            failed_students_list.append((student_name, section, subjects_list))


    print(failed_students_list)

#funcion que muestra todos los estudiantes
def show_all_students():

    if not list_dic:
        print("No students registered")
        return #aqui no retornaria nada > none

    for student in list_dic:
        print(student)

