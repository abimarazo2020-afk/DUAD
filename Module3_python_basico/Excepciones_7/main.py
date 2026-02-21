'''               EXCEPCIONES                  '''

'''Esto no es una excepción ya que el código nunca llega a ejecutarse:'''

#  def main():
#     print('Ejecutando...')
#     &^&*&^*&^


#  if __name__ == '__main__':
# 	 main()


#R/
# File "c:\Users\alekc\repos\d0ad\Secciones\Excepciones\video.py", line 3
# (&&^)
# ^
# SyntaxError: invalid syntax





'''Ahora veamos este ejemplo, digamos que intentamos accesar a un índice que no existe en una lista: '''

# def main():
# 	my_4_elements = ["One", "Two", "Three", "Four"]

# 	print(my_4_elements[3])
# 	print(my_4_elements[4])


# if __name__ == '__main__':
# 	main()
    
#R/
#  Four
# Traceback (most recent call last):
# File "c:\Users\alekc\repos\d0ad\Secciones\Excepciones\index_out_of_range.py", line 4, in <module>
# print(my_4_elements[4])
# ~~~~~~~~~~~~~^^^
# IndexError: list index out of range


#Aqui podemos ver que si se corre el primer print y luego sale el error 






'''Veamos otro ejemplo donde el primer string se logra convertir pero el segundo no y nos da execption'''

# def main():
# 	my_first_string = "2"
# 	my_second_string = "Hello"
    
# 	my_first_int = int(my_first_string)
# 	print(my_first_int + 2)
    
# 	my_second_int = int(my_second_string)
# 	print(my_second_int + 2)


# if __name__ == '__main__':
    # main()

# #R/

# 4
# Traceback (most recent call last):
# File "c:\Users\alekc\repos\d0ad\Secciones\Excepciones\int.py", line 7, in <module>
# my_second_int = int(my_second_string)
# ^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'Hello'
    


'''                            TRY AND EXCEPT                    '''


def main():
    my_second_string = 'Hello'

    try:
        my_second_int = int(my_second_string)
        print(my_second_int + 2)
    except ValueError:
        print('Hubo un error al convertir este string a numero!')
  

if __name__ == '__main__':
    main()


#R/
#Hubo un error al convertir este string a numero!

#Si el try no se cumple nos va a retornar el except
#mismo ejemplo de arriba pero con el try and except


'''Ejemplo usando el identificador de error as'''


def main():
    my_second_string = 'Hello'

    try:
        my_second_int = int(my_second_string)
        print(my_second_int + 2)
    except ValueError as ex:
        print('Hubo un error al convertir este string a numero!')
        print(ex)
  

if __name__ == '__main__':
    main()

#R/ 
# Hubo un error al convertir este string a numero!
# invalid literal for int() with base 10: 'Hello'


'''Otro ejemplo con as identificador '''

def main():
  my_second_string = 'Hello'

  try:
    my_second_int = int(my_second_string)
    print(my_second_int + 2)
  except ValueError as error:
    print(f'Hubo un error al convertir este string a numero: {error}')
    
if __name__ == '__main__':
    main()


#R/
#Hubo un error al convertir este string a numero: invalid literal for int() with base 10: 'Hello’



'''                           EJEMPLOS CON VARIOS EXCEPTS                           '''

def main():
    my_list = [
      '2',
      'Hello'
    ]
    index_to_use = 4
    
    try:
      list_element_to_convert = my_list[index_to_use]  #Intenta acceder al elemento de my_list en la posición 4. pero no existe
      element_to_int = int(list_element_to_convert)
      print(element_to_int)
    except IndexError as error:
      print(f'El indice a usar no existe en la lista. Error: {error}')
    except ValueError as error:
      print(f'El elemento de la lista no es un numero valido. Error: {error}')


if __name__ == '__main__':
    main()

#R/
#Hubo un error al convertir este string a numero: invalid literal for int() with base 10: 'Hello'
#El indice a usar no existe en la lista. Error: list index out of range




'''                           Ejemplos usando 'Exception'                   '''


def main():
    my_list = [
      '2',
      'Hello'
    ]
    index_to_use = 4
    
    try:
      list_element_to_convert = my_list[index_to_use]
      element_to_int = int(list_element_to_convert)
      print(element_to_int)
    except Exception as error:
      print(f'Ha ocurrido un error: {error}')


if __name__ == '__main__':
    main()

#R/ 
#Ha ocurrido un error: list index out of range, esto no nos dice el tipo de error 



'''otro ejemplo con exception'''

def main():
    my_list = [
      '2',
      'Hello'
    ]
    index_to_use = 1
    
    try:
      list_element_to_convert = my_list[index_to_use]
      element_to_int = int(list_element_to_convert)
      print(element_to_int)
    except Exception as error:
      print(f'Ha ocurrido un error: {error}')


if __name__ == '__main__':
    main()

#R/
#Ha ocurrido un error: invalid literal for int() with base 10: 'Hello’



'''Ejemplo con variable que no existe fuera del except'''

def main():
    my_list = [
      '2',
      'Hello'
    ]
    index_to_use = 4
    
    try:
      list_element_to_convert = my_list[index_to_use]
      element_to_int = int(list_element_to_convert)
    except Exception as error:
      print(f'Ha ocurrido un error: {error}')
    
    print(element_to_int)


if __name__ == '__main__':
    main()

#R/
#Ha ocurrido un error: list index out of range
#Traceback (most recent call last):
#File "c:\Users\alekc\repos\d0ad\Secciones\Excepciones\variables_in_try.py", line 10, in <module>
#print(element_to_int)
#^^^^^^^^^^^^^^
#NameError: name 'element_to_int' is not defined

#Aqui el error es la variable


'''Try except general para el programa, y try except especificos para cada funcion'''


def function_1():
    try:
        some_logic_with_value_errors()
    except ValueError as ex:
        print(f'An error ocurred in function_1')


def function_2():
    try:
        some_logic_with_index_errors()
    except IndexError as ex:
        print(f'An error ocurred in function_2')


def main():
    try:
        function_1():
        function_2():

    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')


if __name__ == '__main__':
    main()



''' 
Nunca debemos usar un except para un happy path.
Está muy mal visto ya que está en contra del uso de la sintaxis. EJEMPLO:'''

#INCORRECTO:

name = input("Ingrese su nombre: ")
try:
    int(name)
      # unhappy path
    print("Su nombre no puede ser un numero!")
except Exception as error:
        # happy path
    edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
    empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")


#CORRECTO

try:
    name = input("Ingrese su nombre: ")
    if name.isdigit():
      raise ValueError()
except Exception as error:
      # unhappy path
    print("Su nombre no puede ser un numero!")

# happy path
edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")




'''            EJEMPLOS CON EL RAISE                      '''

'''Por ejemplo, en este código le pedimos la edad al usuario.
Tenemos un try - except en caso de que el usuario no ingrese un número.
Pero también hacemos raise de un ValueError en caso de que el número no esté dentro del rango de 1 a 100.
Luego el except de ese ValueError le hace raise a la misma excepción para que lo atrape el except de afuera y el programa se cierre.'''

def ask_for_user_information():
    try:
        age = int(input('Ingrese su edad'))
        if age < 1 or age > 100:
            raise ValueError()

    except ValueError as ex:
        print("Ingrese una edad valida!")
        raise ex


def main():
    try:
        ask_for_user_information()
        # create_order()

    except Exception as ex:
        exit()


if __name__ == '__main__':
    main()

#Va brincando de except en except por las funciones