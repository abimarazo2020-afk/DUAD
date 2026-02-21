''' A diferencia de las listas tienen un key no un indice.
se coloca el key y luego el valor del key, se dividen por :'''

my_first_dictionary = {
	"key": 5,
	"other_key": "Hello again!",
	"final_key": 98,
}

print(my_first_dictionary["other_key"]) #aqui accesamos exactamente a la key "other_key"

#r/ Hello again!

my_first_dictionary = {
	"key": 5,
	"other_key": "Hello again!",
	"final_key": 98,
    "clase_dics": 99,
}

print(my_first_dictionary["clase_dics"]) 

#r/ 99


# # '''Estructuras mas complejas con listas'''

#Aqui vemos que condo_houses es una lista
#cada casa es un diccionario.
#dentro de ese diccionario vemos que rooms: es una lista de strings
#se pueden combinar de esta manera.


condo_houses = [
	{
		"number": 93,
		"area_m2": 125,
		"rooms": [
			"living_room",
			"kitchen",
			"main_sleeping_room",
			"second_sleeping_room",
			"bathroom",
		],
	},
	{
		"number": 95,
		"area_m2": 125,
		"rooms": [
			"living_room",
			"kitchen",
			"main_sleeping_room",
			"second_sleeping_room",
			"third_sleeping_room",
			"bathroom",
		],
	},
]

print(condo_houses[1]['rooms'][4]) #Asi se accede a las casas
 #Aqui va a imprimir la segunda casa porque empieza en 0 
#con la room numero  4  que empieza en 0


#ANOTHER EXAMPLE:

new_dictionary = {'Key_1': 'valor 1'}

print(new_dictionary['Key_1'])



'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


'''Que pasa si se intenta acceder a un key que no existe?'''
#Nos va a botar el programa.

'''             Para esto vamos a utilizar un metodo que se llama get            '''

#EXAMPLE:

course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('description'))



'''Ahora que pasa aqui si le decimos que nos de un key que no existe?
El programa nos va retornan un none, no se va a crashear'''





 #EXAMPLE SIN GET:


course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information['description'])




'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


'''                             Iteracion de diccionarios                               '''


#Hay varias maneras en las que se pueden iterar los diccionarios
#se puden iterar los keys y los values juntos o se pueden iterar por separado


'''items iteracion'''

#EXAMPLE:

europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country, capital in europe_capitals_by_country.items():
  print(f'{country} : {capital}')

#Esta iteracion me deja recorrer el key y el value y imprimo los dos.




'''Ejemplo con iteracion directa erroneo'''


new_dictionary = {
  'Key_1': 'valor 1',
  'key_2': 'valor 2',
  'key_3': 'valor 3',
  }

for item in new_dictionary:
  print(item)

#R/ key_1
#   key_2
#   key_3


#Este nos va a imprimir solo el key
#R/ solo retorna "key_1" "key_2" "key_3" no los valores del key
#Por esto se usa item como en el ejemplo de arriba

'''La forma correcta seria: '''

for key, valor in new_dictionary.items():
  print(key)
  print(valor)



#Another example:

alumnos = {
    "Ana": 20,
    "Luis": 22,
    "María": 19
}


for nombre, edad in alumnos.items():
    print(nombre, "tiene", edad, "años")





'''Metodo keys'''

#Nos retorna solo el key

for key in new_dictionary.keys():
  print(key)




'''Metodo Values'''

#nos retorna solo los values

for values in new_dictionary.values():
  print(values)



#ANOTHER EXAMPLE CON EL ITEMS:

europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country, capital in europe_capitals_by_country.items():
  print(f'{country} : {capital}')


#EXAMPLE CON EL KEYS:

europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country in europe_capitals_by_country.keys():
  print(country)



# #EXAMPLE CON EL VALUES:

europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for capital in europe_capitals_by_country.values():
  print(capital)




'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''                                   AGREGAR DATOS                             '''

#No se usa append.
#Con los diccionarios es un poco diferente, se hace como si fuera una asignacion.
#Debido a que los datos de los diccionarios están atados a keys
# debemos accesar a la key que queremos llenar (aunque no exista) y darle un valor



#EJEMPLO CON UN KEY QUE NO EXISTE AUN

user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

user_data['password'] = 'WinterIsComing2023'
print(user_data)

#Aqui se crea el key password y se le asigan el valor 

#R/   {'full_name': 'John Snow', 'email': 'j.snow@gmail.com', 'password': 'WinterIsComing2023'}




#EJEMPLO DE ALGO QUE SE PUEDA AGREGAR

for number in range(0, 4): # 0 1 2 3
  user_data[str(number)] = 'san jose'

print(user_data)

# esto agrega 4 valores con el nombre de san jose
# el rango seria la posicion verdad 

#R/ {'full_name': 'John Snow', 'email': 'j.snow@gmail.com', 'password': 'WinterIsComing2023', '0': 'san jose', '1': 'san jose', '2': 'san jose', '3': 'san jose'} 

'''                                      Agregar datos                             '''

'''
Debido a que los datos de los diccionarios están atados a keys, 
debemos accesar a la key que queremos llenar (aunque no exista) y darle un valor:'''



user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

user_data['password'] = 'WinterIsComing2023'
print(user_data)

# R/
# {'full_name': 'John Snow', 'email': 'j.snow@gmail.com', 'password': 'WinterIsComing2023'}









"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""


'''                                ELEIMINAR DATOS                                    '''


'''Al igual que con las listas, podemos usar el método pop para eliminar el elemento de un key especifico:
Este método también retorna el elemento eliminado.'''

#Se hacae usando el key y se puede huardar en una variable para usarlo si queremos
#los diccionarios no tienen un orden

student_information = {
	'first_name': 'Harry',
	'last_name': 'Potter',
	'age': 17,
}

deleted_item = student_information.pop('last_name')
print(student_information)
print(f'Deleted item: {deleted_item}')




# #EXAMPLES CHAT GPT:

# ''' Dado este diccionario: 
# 1 Si el stock es mayor a 0, imprime "Producto disponible"
# 2  Resta 1 al stock (simula una compra)'''

producto = {
    "nombre": "Laptop",
    "precio": 1200,
    "stock": 5
}


if producto["stock"] > 0:
    print("Producto disponible")
    producto["stock"] -= 1



#another exercise but with lists

'''Crea un diccionario llamado persona que tenga:
nombre
una lista de hobbies
'''

persona = {
    "nombre": "Ana",
    "hobbies": ["leer", "correr", "dibujar"]
}

#imprimer todos los hobbies
print(persona['hobbies'])

#recorre todos los hobbies y los imprime
for hobby in persona['hobbies']:
    print(hobby)

#accede solo al primer elemento de la lista y lo imprime
print(persona["hobbies"][0])

#agrega un elemento a la lista
persona["hobbies"].append('cocinar')
print(persona['hobbies'])





animales = [
    {'animal': 'perro','cantidad_de_patas': 4},
    {'animal': 'pajaro','cantidad_de_patas': 2},
    {'animal': 'canguro','cantidad_de_patas': 2}
]
suma = 0 

for animal in animales:
    print(animal['animal'], 'tiene', animal['cantidad_de_patas'], 'patas')
    suma += animal['cantidad_de_patas']

    if animal['cantidad_de_patas'] == 2:
        print('este animal tiene dos patas',animal['animal'])

print(suma)