"""EJERICIO#5
Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.
"""

total_notes = int(input('Ingrese su cantidad de notas:'))
note_counter = 1
disapproved_quantity = 0
approved_quantity = 0
approved_average = 0
disapproved_average = 0
total_average = 0
total_sum = 0
approved_sum = 0
disapproved_sum = 0
#si solo ponemos una suma esta mal porque no cuenta los valores de las notas si no la cantidad de notas


while note_counter <= total_notes:
    current_note = int(input(f'Enter your note #{note_counter}:'))
    note_counter = note_counter+1
    total_sum = total_sum + current_note

    if(current_note >= 70):
        approved_quantity = approved_quantity + 1
        approved_sum = approved_sum + current_note

    else:
        disapproved_quantity = disapproved_quantity + 1
        disapproved_sum = disapproved_sum + current_note


total_average = total_sum / total_notes
print(total_average)

if approved_quantity > 0:
    approved_average = approved_sum / approved_quantity

if disapproved_quantity < 0:
    disapproved_average = disapproved_sum / disapproved_quantity


print(f'The student has this number of passing grades. {approved_quantity}')
print(f'The student has this number of failing grades {disapproved_quantity}')
print(f'The average passing grade is:: {approved_average}')
print(f'The average number of failing grades is: {disapproved_average}')
print(f'This is the overall average {total_average}')