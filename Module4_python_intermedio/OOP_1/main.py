'''                                                     PROGRAMACION ORIENTADA A OBJECTOS                                            '''


'''COMO CREAR CLASES Y OBJECTOS'''

#Para declarar una clase usamos la palabra class seguida de su identificador.

class Car:
  pass
  
  
  
  

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''





'''Para crear un objeto, debemos llamar a la clase como si fuera una función que retornara ese nuevo objeto:'''


class Car:
  pass      #signfica no hacer nada porque aun no hay ni metodos ni atributos


my_car = Car() #Aqui se crea el un objecto(una instancia)  y se llama my_car
print(my_car)

#R/
# <__main__.Car object at 0x000001A3F5C9B8E0> 
#Car object → es un objeto de la clase Car. 0x000001A3F5C9B8E0 → es la dirección de memoria del objeto.

# Car() Le dices a Python: 👉 “Crea un nuevo objeto usando el molde Car”.

# my_car ahora es un objeto tipo Car. Es una variable que guarda ese objeto. Es como ponerle un nombre a ese carro para poder usarlo después.

# class Car: → plano de un carro

# Car() → fabricar un carro usando ese plano

# my_car → el nombre que le pones a ese carro




'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''                          Con una sola clase puedo crear cuantas instancias yo quiera.                   '''


class Car:
  pass


my_car = Car()

my_car_2 = Car()

print(my_car)
print(my_car_2)


#R/
# <main.Car object at 0x00000198F3D7ED50>
# <main.Car object at 0x00000198F3D7EDD0>



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''




'''                                                          ATRIBUTOS                                                          '''


#Como mencionamos antes, un atributo es una variable dentro de un objeto.
#Así todos los objetos que se creen usando ese molde tendrán esos atributos.


class Car:
	wheel_number = 4
	
#Aquí estamos definiendo que todos los objetos de tipo Car tendrán 4 ruedas.

#Ahora podemos accesarlo una vez que instanciemos un Car.

class Car:
	wheel_number = 4


my_car = Car()
print(my_car.wheel_number)   #IMPORTANTE poner my_car. para accederlo



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''Al igual que con las variables, también podemos asignarle nuevos valores a los atributos.'''


class Car:
	wheel_number = 4


my_car = Car()
my_car.wheel_number = 6
print(my_car.wheel_number)

#R/
#6

#Recordemos que, a pesar de venir del mismo molde, los objetos son entidades independientes.



'''Esto significa que distintos objetos de la misma clase pueden tener distintos valores en sus atributos.'''

class Car:
	wheel_number = 4


my_car = Car()

my_truck = Car()
my_truck.wheel_number = 6

my_bigger_truck = Car()
my_bigger_truck.wheel_number = 8


print(my_car.wheel_number)
print(my_truck.wheel_number)
print(my_bigger_truck.wheel_number)

#R/

# 4
# 6
# 8

#Varios objectos, mismo atributo pero con diferente valor 




'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''




'''                                                            METODOS                                                  '''

#Como mencionamos antes, un método es una función dentro de un objeto (como el append de las listas).


"""Los métodos se declaran exactamente igual que una función con la diferencia de que su primer parámetro siempre será self 
(más adelante veremos para qué se usa"""
		
class Car:
	wheel_number = 4

	def my_first_method(self):
		print("Hello OOP World!")


my_car = Car()
my_car.my_first_method()
		
#R/
#Hello OOP World!




'''Al igual que las funciones, los métodos pueden tener cuantos parámetros queramos después del self.
Eso sí, el self es esencial y no se puede quitar ni reemplazar.'''


class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles and {crashes} crashes")
		
		
my_car = Car()
my_car.show_history(45000, 2) #Aqui es donde asignamos el valor de miles y crashes


#R/
# This car has 45000 miles and 2 crashes



'''EJEMPLO UTILIZANDO EL SELF PARAMETER'''

class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
my_car = Car()
my_car.show_history(45000, 2)

#R/
#This car has 45000 miles, 2 crashes and 4 wheels

#Aquí estamos usando el self para acceder al valor del atributo wheel_number del Car que llame a ese método en el futuro.
#  tomando en cuenta lo que vimos acá, dos objetos de tipo Car pueden tener valores de wheel_number distintos. 
#  Para eso usamos el self! Para acceder al valor del objeto específico que esté llamando al método.



'''EJEMPLO CON MAS OBJECTOS'''


class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
my_car = Car() # aqui se crea el objecto

my_truck = Car() # aqui se crea el objecto
my_truck.wheel_number = 6 #aqui se le asigna un valor diferente a wheels

my_bigger_truck = Car()
my_bigger_truck.wheel_number = 8


my_car.show_history(45000, 2) #aqui se asigna el valor
my_truck.show_history(45000, 2)
my_bigger_truck.show_history(45000, 2)

#R/
# This car has 45000 miles, 2 crashes and 4 wheels
# This car has 45000 miles, 2 crashes and 6 wheels
# This car has 45000 miles, 2 crashes and 8 wheels





'''Digamos que. siguiendo la analogía de la fábrica, Car es una fábrica que solo fabrica automóviles con motor de gasolina diesel.

Pero también le dan la opción a sus clientes de cambiarle ese motor por uno de gasolina súper por un costo de $2000.

Esta opción solo está disponible una vez que el automóvil está fabricado.
Entonces podemos decir que los Car pueden tener un atributo de gas_type, y por defecto debe ser “diesel”.

Y podemos agregar un método que cambie el gas_type de “diesel” a “super” para los clientes que quieran pagar $2000 por el cambio de motor.'''


class Car:
	wheel_number = 4
	gas_type = "diesel"
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
	def upgrade_engine(self):
		if self.gas_type == "diesel":
			print("Cambiando el motor diesel por uno de gasolina super por $2000...")
			self.gas_type = "super"
		else:
			print("Este automovil ya tiene un motor de gasolina super!")
			
			

print("Primer auto")
my_car_1 = Car()
print("Auto fabricado")
print(my_car_1.gas_type) #imprimi disel por defecto de fabrica

my_car_1.upgrade_engine() #aqui le cambiamos el gas_type

print("Auto mejorado")
print(my_car_1.gas_type) #imprime super porque se cambio 


my_car_1.upgrade_engine() # se vuelve a cambiar el gas_type

print("Segundo auto")
my_car_2 = Car()
print(my_car_2.gas_type) #por ultimmo y ppr defecto queda disel

#R/
# ✅
# Primer auto
# Auto fabricado
# diesel
# Cambiando el motor diesel por uno de gasolina super por $2000...
# Auto mejorado
# super
# Este automovil ya tiene un motor de gasolina super!
# Segundo auto
# diesel





'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''                                                LOS CONSTRUCTORES                                                '''




'''
El constructor es el método que se ejecuta por defecto cada vez que instanciamos una clase.
Por ejemplo cuando hacemos esto: '''

class Person():
	pass


person_1 = Person()



'''METODO _init_ '''

class Person():
	def __init__(self):
		print("Ha nacido una persona!")


person_1 = Person()
person_2 = Person()

#R/
# Ha nacido una persona!
# Ha nacido una persona!


'''Desde el constructor también podemos crear atributos, como en cualquier otro método.'''


class Person():
	def __init__(self):
		print("Ha nacido una persona!")
		self.age = 0

person_1 = Person()
print(person_1.age)

#R/
# Ha nacido una persona!
# 0


'''EJEMPLO CON PARAMETROS PERO MAL HECHO'''

class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.age = 0

person_1 = Person() #Aqui esta el error porque no le asignamos nada a name
print(person_1.age)

#R/
# Traceback (most recent call last):
# File "c:\Users\alekc\repos\d0ad\OOP\attribute.py", line 6, in <module>
# person_1 = Person()
# ^^^^^^^^
# TypeError: Person.init() missing 1 required positional argument: 'name'

# Estos parámetros serán necesarios para instanciar la clase, ya que el constructor es el método que se llama al hacerlo.
# Así que debemos especificarlos a la hora llamar Person().



'''EJEMPLO BIEN HECHO'''

class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.age = 0

person_1 = Person("John")
print(person_1.age)

#R
# Ha nacido una persona llamada John!
# 0


'''

Ahora, los parámetros del constructor no se convierten automáticamente en atributos…
Son como parámetros comunes y corrientes: variables locales que dejan de existir apenas termine su scope (ver acá).'''

class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.age = 0

person_1 = Person("John")
print(person_1.age) #este esta bien porque si se creo el atributo self.age
print(person_1.name) #aqui esta el error porque name es una variable,osea un parametro nada mas no un atributo creado


#R/
# Ha nacido una persona llamada John!
# 0

# Traceback (most recent call last):
# File "c:\Users\alekc\repos\d0ad\OOP\attribute.py", line 8, in <module>
# print(person_1.name)
# ^^^^^^^^^^^^^
# AttributeError: 'Person' object has no attribute 'name'


'''Si queremos que esos parámetros (que son variables comunes y corrientes) se conviertan en atributos,
tenemos que guardamos como atributos. Usando el self.'''

class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name #estos son atributos creados desde el constructor
		self.age = 0

person_1 = Person("John")
print(person_1.age)
print(person_1.name)


'''                  IMPORTANTE             '''

'''
MUY IMPORTANTE!
name no es lo mismo que self.name
age no es lo mismo que person_1.age
variable no es lo mismo que self.variable'''


class Person():
	def __init__(self, name):
		self.name = name #estos son atributos creados desde el constructor
		self.age = 0    #estos son atributos creados desde el constructor
		age = 56

person_1 = Person("John")
age = 34

print(person_1.age) #solo se imprime self.age porque es el atributo creado

# R/
# 0


class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0
		age = 56

person_1 = Person("John")
age = 34

print(age) #aqui solo estamos imprimiendo la variable age que esta abajo y afuera del metodo

#R/
#34



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''                                                              EJEMPLOS EXTRA                                          '''


'''Acá un ejemplo de otra clase Car con multiples atributos que se definen desde su constructor.'''

class Car:
  def __init__(self, brand, line, model, color):
    self.brand = brand   #estos son atributos creados desde el constructor
    self.line = line     #estos son atributos creados desde el constructor
    self.model = model   #estos son atributos creados desde el constructor
    self.color = color   #estos son atributos creados desde el constructor


my_audi = Car("Audi", "A4", 2023, "Red")
my_bmw = Car("BMW", "X5", 2021, "Green")
my_ferrari = Car("Ferrari", "Enzo", 1999, "Red")




'''También podemos usar el constructor para definir o inicializar otros atributos que no necesariamente estamos pasando como parámetros, o para definir lógica que necesitamos ejecutar al crear los objetos.
Por ejemplo, aquí tenemos una clase de PhotographyCamera con una lista de Photos y un método para tomar fotos y agregarlas a esta lista:'''

class PhotographyCamera:
	photographies = []

	def __init__(self, storage_size_in_mb):
		# each photo takes around 10mb
		self.max_photographies = storage_size_in_mb / 10
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		
kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
print(kodak_camera.photographies)