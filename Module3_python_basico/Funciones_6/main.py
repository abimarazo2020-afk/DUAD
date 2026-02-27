'''                                      FUNCIONES                              ''' 




'''Por ejemplo, puedo crear una función que llame un print para imprimir Hello World y Mi primera funcion. 
A esta función la llamaré print_hello_world'''

# def print_hello_world():
	# print("Hello World!")
	# print("Mi primera funcion")


# Si ejecutamos esto, no pasará nada.
# Esto es porque solo estamos creando o definiendo la función, pero nunca la estamos ejecutando.




'''Para ejecutarla, o “llamarla”, es exactamente igual que hacer un print:
 usando su identificador seguido de paréntesis. Es decir print_hello_world():'''


def print_hello_world():
	print("Hello World!")
	print("Mi primera funcion")

print_hello_world()

# print_hello_world() Esto llama la funcion y asi es como la imprimimos






'''podriamos hasta meter un codigo en una funcion'''

# Antes (sin funciones) 

worked_hours = int(input("Ingrese sus horas trabajadas: "))
hour_rate = int(input("Ingrese su tarifa por hora: "))

salary = worked_hours * hour_rate

print(f'Su salario sera de {salary}')



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#Después (convertido a función) 

def calculate_salary():
	worked_hours = int(input("Ingrese sus horas trabajadas: "))
	hour_rate = int(input("Ingrese su tarifa por hora: "))
	
	salary = worked_hours * hour_rate
	
	print(f'Su salario sera de {salary}')


calculate_salary()



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''Funciones mal y bien ordenadas'''

#Mal ordenadas

# def function_2():
# 	print('Ejecutando 2')
# main()

# def main():
# 	function_1()
# 	function_2()
# 	function_3()

# def function_1():
# 	print('Ejecutando 1')
# def function_3():
# 	print('Ejecutando 3')
	

#Bien ordenadas

def function_1():
	print('Ejecutando 1')


def function_2():
	print('Ejecutando 2')


def function_3():
	print('Ejecutando 3')


def main():
	function_1()
	function_2()
	function_3()


main()



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''Funciones con parametros y retornos'''

#ESTRUCUTURA 

def nombre(parameter1, parameter2, etc):
	# instruccion 1
	# instruccion 2
	# instruccion 3
	
	return output



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''    PARAMETROS       '''


#EJEMPLO CON 3 PARAMETROS

def print_parameters(parameter_1, parameter_2, parameter_3):
	print(f'This is parameter 1: {parameter_1}')
	print(f'This is parameter 2: {parameter_2}')
	print(f'This is parameter 3: {parameter_3}')


print_parameters(50, 'Hello', True) #AQUI ES DONDE LE ASIGNAMOS UN VALOR A LOS PARAMETROS


# R/
# This is parameter 1: 50
# This is parameter 2: Hello
# This is parameter 3: True


#podemos cambiar los parametros y se deberian de imprimir los primeros y segundos valores 
#que se le asigno a los parametros


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


#PARAMETROS OPCIONES

def print_parameters(parameter_1, parameter_2, parameter_3):
	print(f'This is parameter 1: {parameter_1}')
	print(f'This is parameter 2: {parameter_2}')
	print(f'This is parameter 3: {parameter_3}')


# print_parameters(50, 'Hello')	

#ESTO ME DARIA UN ERROR DE QUE FALTA UN PARAMETRO:

#R/ 
#  print_parameters(50, 'Hello')
#     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
# TypeError: print_parameters() missing 1 required positional argument: 'parameter_3'


'''Se soluciona con que le podamos dar un valor provisional a un parametro'''


def print_parameters(parameter_1, parameter_2, parameter_3='Abigail'): 
	print(f'This is parameter 1: {parameter_1}')
	print(f'This is parameter 2: {parameter_2}')
	print(f'This is parameter 3: {parameter_3}')


print_parameters(50, 'Hello')


#ANOTHER EXAMPLE:


def print_sum_of_numbers(number_a, number_b=5):
	print(number_a + number_b)


print_sum_of_numbers(4) # 4 ES EL VALOR QUE SE LE ASIGNA A number_a

#R/ 9

print_sum_of_numbers(4, 20) #Aqui cambiamos el valor de el number_b

#R/ 24



'''       RETORNOS       '''


# EJEMPLO, podemos crear una función que sume tres números y retorne su resultado:


def sum_three_numbers(number1, number2, number3):
	return number1 + number2 + number3


result = sum_three_numbers(600, 700, 800) #Aqui guardamos en una variable la suma y estos son los parametros
print(result)


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


#EJEMPLO CON VARIOS RETURN:


def sum_three_numbers(number1, number2, number3):
	if number1 == 1000:
		return number1
	
	return number1 + number2 + number3 #Esto no se correria


result = sum_three_numbers(1000, 700, 800) 
print(result)


#R/ 1000 

#solo va a correr el primer return 





'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#OTRO EJEMPLO
# podemos crear una función que encuentre el máximo de 2 números y lo retorne:


def get_max_of_two_numbers(number1, number2):
  if number1 > number2:
    return number1

  return number2


print(get_max_of_two_numbers(3, 7))


'''
Esta función tiene 2 parámetros, number1 y number2.
Si number1 es mayor a number2, retorna number1.
El return hace que la función termine. Su output sale y el resto no se ejecuta. 
Por eso es que no es necesario el else en este caso. 
Sabemos que si la primera condición se cumple, se ejecuta el return y el segundo return nunca se ejecutará.
Si no es así, retorna number2.'''


'''Podemos notar es que estamos encadenando dos funciones, print y get_max_of_two_numbers.
Esto es porque ya sabemos que esa función va a retornar un valor.
Y una función ejecutada es igual a utilizar un valor o una variable.
Podemos usar llamados a funciones como parámetros para otras funciones, 
ya que el código se ejecutará de adentro hacia afuera.'''



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''




#EJEMPLO IGUAL PERO CON VARIABLE:

def get_max_of_two_numbers(number1, number2):
  if number1 > number2:
    return number1

  return number2


result = get_max_of_two_numbers(4, 15)
print(result)




'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''Si al nombrar una función tenemos que usar “y”, lo mejor es dividir esa función en dos funciones.'''


#EJEMPLO PARA NO USAR 'Y'
#Por ejemplo, si tengo un código en el que calculo el promedio de notas de todos varios estudiantes 
#y reviso si se eximieron


# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = (juan_scores["spanish_score"] + juan_scores["science_score"] + juan_scores["history_score"]) / 3
sofia_scores["average_score"] = (sofia_scores["spanish_score"] + sofia_scores["science_score"] + sofia_scores["history_score"]) / 3
paul_scores["average_score"] = (paul_scores["spanish_score"] + paul_scores["science_score"] + paul_scores["history_score"]) / 3

juan_scores["is_exempted"] = juan_scores["average_score"] > 70
sofia_scores["is_exempted"] = sofia_scores["average_score"] > 70
paul_scores["is_exempted"] = paul_scores["average_score"] > 70


'''Podemos notar que ese calculo de (spanish_score + science_score + history_score) / 3 se repite para cada estudiante.
Tambien estamos repitiendo la validación de si el average_score > 70.
Además puede ser confuso y repetitivo de leer ya que estamos haciendo varias cosas a la vez.
Lo mejor dado estas circunstancias es dividir esto en funciones reutilizables más pequeñas.'''


#EJEMPLO CON FUNCIONES


def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = get_average_score(juan_scores)
sofia_scores["average_score"] = get_average_score(sofia_scores)
paul_scores["average_score"] = get_average_score(paul_scores)

juan_scores["is_exempted"] = is_student_exempted(juan_scores)
sofia_scores["is_exempted"] = is_student_exempted(sofia_scores)
paul_scores["is_exempted"] = is_student_exempted(paul_scores)


'''Incluso podemos hacer este código aun mejor convirtiendo estos diccionarios en una lista
y haciendo un ciclo que haga lo mismo para todos:'''


def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
students = [
  {
    "name": "Juan",
		"spanish_score": 75,
		"science_score": 95,
		"history_score": 54,
	},
  {
    "name": "Sofia",
		"spanish_score": 64,
		"science_score": 56,
		"history_score": 98,
	},
  {
    "name": "Paul",
		"spanish_score": 72,
		"science_score": 75,
		"history_score": 79,
	}
]

# Averages
for student in students:
  student["average_score"] = get_average_score(student)
  student["is_exempted"] = is_student_exempted(student)
  print(student["name"], " is_exempted is ", student["is_exempted"])