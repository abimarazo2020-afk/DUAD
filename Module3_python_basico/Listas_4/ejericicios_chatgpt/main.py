# '''Ejercicios con for directo (recomendado para empezar)'''


# '''Pide al usuario 6 palabras y guarda solo las que tengan más de 5 letras en una nueva lista.'''

# new_list = [] 
# second_list = []

# for i in range(6):
#     word = str(input(f'Ingrese su palabra {i + 1}:'))
#     new_list.append(word)

# for element in new_list:
#     if len(element) > 5:
#         second_list.append(element)

# print(second_list)




# '''Pide al usuario 5 números y muestra una lista solo con los números pares.'''

# list_three = []
# new_list_three = []

# for i in range(5):
#     number = int(input(f'Ingese su numero {i + 1}:'))
#     list_three.append(number)

# for element in list_three:
#     if element % 2 == 0:
#         new_list_three.append(element)

# print(new_list_three)





'''Pide al usuario 5 palabras y crea una nueva lista con esas palabras en mayúsculas.'''

# list_four = []
# new_list_four = []

# for i in range(5):
#     word = str(input(f'Ingrese la palabra {i + 1}:'))
#     list_four.append(word)

# print(list_four)

# for element in list_four:
#     new_word = element.upper()
#     new_list_four.append(new_word)

# print(new_list_four)


'''Pide al usuario 4 palabras y muestra cuántas letras tiene cada una.'''

# list_five = []
# new_list_five = []

# for i in range(4):
#     word = str(input(f'Ingrese su palabra {i + 1}:'))
#     list_five.append(word)

# for element in list_five:
#     print(len(element))


'''Pide al usuario 5 palabras y guarda en una nueva lista solo las palabras que empiecen con una vocal.'''

# list_six = []
# vocales_list = []
# vocales = ['a', 'e', 'i', 'o', 'u']
# for i in range(5):
#     word = str(input(f'Ingrese su palabra {i + 1}:'))
#     list_six.append(word)

# for palabra in list_six:
#     if palabra[0] in vocales:
#         vocales_list.append(palabra)
 
# print(vocales_list)




'''                                ITERACION POR INDICE                                  '''
 

'''Multriplica numeros * 2 '''
# numeros = [5, 10, 15, 20]

# for i in range(len(numeros)):
#     numeros[i] = numeros[i] * 2  #esto crea una variable

# print(numeros)


'''Sumar todos los valores'''

# numeros = [4, 5, 6]
# suma = 0 

# for i in range(len(numeros)):
#     suma = suma + numeros[i]

# print(suma)


'''Modificar la lista (sumar 1)'''

# numeros = [1, 2, 3]

# for i in range(len(numeros)):
#     numeros[i] = numeros[i] + 1

# print(numeros)

'''Reemplazar negativos por 0'''

# valores = [5, -3, 2, -1]

# for i in range(len(valores)):
#     if valores[i] < 0:
#         valores[i] = 0

# print(valores)

'''Reemplazar valores mayores que 10 por 10'''

# numeros = [4, 15, 8, 20, 10]

# for i in range(len(numeros)):
#     if numeros[i] > 10:
#         numeros[i] = 10

# print(numeros)

'''Si el número es par, poner 0.
Si es impar, poner 1.'''

# numeros = [4, 7, 2, 9]

# for i in range(len(numeros)):
#     if numeros[i] == 0:
#         numeros[i] = 0

#     else:
#         numeros[i] = 1

# print(numeros)


numeros = [2, 5, 8, 3] 

for number in numeros:
    if numeros % 2 == 0:
        numeros.append(number)

    