"""Iteracion Directa"""

my_favorite_records = [
    'Dark Side Of The Moon',
    'Fear of a Blank Planet',
    'Signify',
]

for record in my_favorite_records:  # Asigna cada elemento de la lista a record
    if record == 'Signify':
        print('Es el elemento más importante')
    elif record == 'Dark Side Of The Moon':
        print('Es un sitio interesante')
    else:
        print('No existe miedo')

print(f'Todos los elementos son: {my_favorite_records}')



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''Iteracion por indice''' #hacer cambios en la propia lista, directo en los iterables
my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index in range(0, len(my_favorite_records)):
    # print(index)
    #print(my_favorite_records[1]) #Aqui accedemos al indice 1 
    #print(my_favorite_records[index]) #Imprimimos el primer resultado pero por index
    #my_favorite_records[index] = 'Hello' #por indice cambiamos todos los elementos a hello 
	record = my_favorite_records[index] #asignamos los elementos a record no el indice
	print(f'Record {index}: {record}')


"""range se utiliza para crear el contador de los numeros que vamos corriendo.
Aqui con el range le decimos que cree una lista de numerosde 0 a la cantidad de elementos
 de my favorite records asi que crearia el 0,1,2.
Con este indix se puede acceder a los elementos de la lista """






"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""




"""Iteracion por indice pero con el while"""

my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

index = 0
while (index < len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')
	index += 1

# Hace lo mismo que la funcion range pero como si fuera manuelmente, 
# recordemos que el while se usa cuando no hay certeza de cuantas veces se ocupa el ciclo o 
# de  cuantos elementos hay en la lista





"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""





"""Iteracion directa incluyendo el indice """

# '''La función enumerate nos permite combinar ambos métodos en uno.
# Esta se ve elegante y es igual de flexible que la clásica.'''

my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index, record in enumerate(my_favorite_records):
	print(f'Record {index}: {record}')





"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""





"""String iteracion"""

my_string = 'Hola Mundo'

for character in my_string:
    print(character)


"""Podemos acceder a caracteres especificos"""

print(my_string[1]) #daria o como resultado






""""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

'''Rompiendo Ciclos'''

#CUANDO QUEREMOS QUE NUESTRO CICLO SE DETENGA ANTES DE LO ESPERADO
#sE PUEDE USAR CUANDO OCUPAMOS ENCONTRAR ALGO ESPECIFICO Y SI LO ENCUENTRA SE SALE.

colors = [
	'black',
	'yellow',
	'red',
	'blue',
]

for color in colors:
	print(color)
	if color == 'yellow':
		break
      

	'''HACIENDOLO CON UN CONTADOR'''
      
	#Aqui basicamente lo vamos a hacer comparando el contador para que nos haga el break.
	counter = 0
    
	while True:
          print(f'Infinidad {counter}') #cuando llegue a 16 se para el ciclo
          if counter > 15:
                break
          counter += 1
          


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''




'''Adelantando Ciclos'''
#Aqui lo que va a pasar es que cuando llegue a yellow va a pasar al siguiente como omitiendo yellow

colors = [
	'black',
	'yellow',
	'red',
	'blue',
]

for color in colors:
	if color == 'yellow':
		continue

	print(color)