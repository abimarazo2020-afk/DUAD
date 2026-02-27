
'''EJERCICIO#2
Create a program that checks if all elements in a list are positive
Restrictions:
Do not use functions like all()'''


list_two = [1, -3, -15, 56, 8, 9]
positive_elements = []

for elem in list_two:
    if elem > 0:
        positive_elements.append(elem)

    else:
        break

if len(positive_elements) == len(list_two):
    print(True)
    print('All the number are positive')
else:
    print(False)
    print("Not all the number are positive")