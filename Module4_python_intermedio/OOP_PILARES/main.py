'''Por ejemplo, creemos una clase Vehicle que tenga 2 métodos: turn_on y turn_off:'''

class Vehicle:
  is_on = False
  wheel_number = 0

  def turn_on(self):
    self.is_on = True
    print(f"Vehicle with {self.wheel_number} wheels is on")

  def turn_off(self):
    self.is_on = False
    print(f"Vehicle with {self.wheel_number} wheels is off")
    
    
    
'''Ahora creemos 2 clases que hereden de Vehicle:'''
    
    
class Car(Vehicle):
  wheel_number = 4


my_car = Car()
my_car.turn_on()
my_car.turn_off()


class Bike(Vehicle):
  wheel_number = 2


my_bike = Bike()
my_bike.turn_on()
my_bike.turn_off()

#Estas clases heredan todo lo que vehicle tiene.
#Sin embargo, también tienen valores de wheel_number distintos porque sobre-escribieron el de Vehicle.







'''                                    HERENCIA MULTIPLE                             '''


'''Python es de los pocos lenguajes en donde una clase puede heredar de n cantidad de clases y no solo de 1.
Por ejemplo, puedo tener tres clases padre:'''


class WalkerMixin:
  def walk(self):
    print("I'm walking!")

class RunnerMixin:
  def run(self):
    print("I'm running!")

class FlyerMixin:
  def fly(self):
    print("I'm flying!")
    
    
    '''Y una clase que herede de todas a la vez:'''
    
class SuperMan(WalkerMixin, RunnerMixin, FlyerMixin):
  pass

clark_kent = SuperMan() #aqui es donde se crea el objecto
clark_kent.walk() #esto le da habilidad al superman object
clark_kent.run() #esto le da habilidad al superman object
clark_kent.fly() #esto le da habilidad al superman object

#superman combina todas las habilidades en un solo object

# Si hicieras esto:

# w = WalkerMixin()

# ✔ Ahí SÍ crearías otro objeto diferente

# Pero en tu código 👉 no lo hiciste






'''
En caso de que dos (o mas) de estas clases tengan métodos o atributos con el mismo identificador,
la primera tendrá prioridad y sobre-escribirá a las de las posteriores.'''


class ClassA:
  name = "A"

  def my_method():
   print("Hello")


class ClassB:
  name = "B"

  def my_method():
	  print("Goodbye")
		
		
		
class ClassC(ClassA, ClassB):
  def print_name(self):
    print(f"My name is {self.name}")

my_c = ClassC()
my_c.print_name()
my_c.my_method()

#R/ 
# My name is A
# Hello


class ClassC(ClassB, ClassA):
  def print_name(self):
    print(f"My name is {self.name}")

my_c = ClassC()
my_c.print_name()
my_c.my_method()

#R/
# My name is B
# Goodbye


#este ejemplo es para revisar el orden, veamos que en los dos cambian






'''                                CLASES ABSTRACTAS                       '''

from abc import ABC, abstractmethod


class Animal(ABC):
	def breath(self):
		pass

	def born(self):
		pass

	@abstractmethod
	def reproduce(self):
		# Todas las especies de animales deben reproducirse para sobrevivir
		# Pero lo pueden hacer de distintas maneras
		pass

class AsexualAnimal(Animal):
	def reproduce(self):
		print("Reproducing in an asexual manner")

class SexualAnimal(Animal):
	def reproduce(self, mate):
		print(f"Reproducing in a sexual manner with {mate}")

class OtherAnimal(Animal):
	pass


asexual_animal = AsexualAnimal()
asexual_animal.reproduce() # -> Reproducing in an asexual manner 

sexual_animal_a = SexualAnimal()
sexual_animal_b = SexualAnimal()
#sexual_animal.reproduce(sexual_animal_b) # -> Reproducing in a sexual manner with sexual_animal_b

animal = Animal() # va a fallar porque Animal es una clase abstracta
other_animal = OtherAnimal() # va a fallar porque no se sobre-escribió el método reproduce







'''                             Encapsulamiento                                 '''

'''EJERCICIO CON ENCAPSULAMIENTO PERO NO PYTHON '''

class BankAccount():
	balance = 0 # 👉 Ojo: esto es un atributo de clase, no de instancia (aunque luego se usa como si fuera de instancia).
        
        #Private method
	def __substract_balance(self, amount):
		self.balance -= amount
        
        #Private method
	def __add_balance(self, amount):
		self.balance += amount
       
       
	def send_money_to_account(self, account, amount):
		self.__substract_balance(amount)
		account.__add_balance(amount)

# Paso a paso:
# self.__substract_balance(amount)
# Le quita dinero a la cuenta actual
# account.__add_balance(amount)
# Le agrega dinero a otra cuenta

# ✔ account es otro objeto de BankAccount


bank_account = BankAccount() # se crea el objecto con balamce en 0 
bank_account.__add_balance(5000) #🚨 ESTO VA A DAR ERROR, add_balance es privado







'''EJERCICIO ENCAPSULAMIENTO HIPOTETICO PYTHON'''

from datetime import datetime

class Person:
    name: str  # public
    _date_of_birth: datetime  # protected (convención)
    __sex: str  # private

    def __init__(self, name, date_of_birth, sex):
        self.name = name
        self._date_of_birth = date_of_birth
        self.__sex = sex


class Worker(Person):
    def print_date_of_birth(self):
        print(self._date_of_birth)

    def print_sex(self):
        print(self._Person__sex)  # acceso correcto


my_person = Person("Juan", "2003/02/02", "Male")

print(my_person.name)              # ✅ Juan
print(my_person._date_of_birth)   # ✅ FUNCIONA (aunque no recomendado) porque es protected
# print(my_person.__sex)          # ❌ ERROR

#aqui va a funcionar porque creamos un worker y se puede acceder desde las clases hijas
my_worker = Worker("Joan", "1984/05/06", "Female")

my_worker.print_date_of_birth()   # ✅
my_worker.print_sex()             # ✅ ahora funciona




'''Debido a que Python carece de esta protección, (y el ejemplo de arriba es hipotético - en realidad todos los casos funcionarían), lo que se usa como estándar es usar guiones bajos en sus identificadores para especificar su nivel de protección.
name es publico.
_name es protected.
__name es privado.
get_age es publico.
_get_age es protected.
__get_age es privado.
'''


'''                                    ABSTRACION                                                        '''

