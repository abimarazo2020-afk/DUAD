'''Cree una clase base Vehicle con los atributos:
_brand
_year
Agregue un método get_info() que devuelva una descripción del vehículo.
Luego cree dos clases hijas:
Car
Motorcycle
Cada una debe agregar su propio atributo (por ejemplo, doors o type) y
sobrescribir el método get_info() para incluir esta información adicional.'''


class Vehicle():
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        
    def get_info(self):
        return (f"This vehicle was made in the year: {self._year}, and the brand is: {self._brand}")
        
        
class Car(Vehicle):
    def __init__(self, brand, year, steering_wheel, doors): #hay que poner lo atributos del padre en el init
        self.steering_wheel = steering_wheel
        self.doors = doors
        super().__init__(brand, year)
        
    def get_info(self):
        return (f"This car was made in the year: {self._year}, and the brand is: {self._brand}. This car has a {self.steering_wheel} steering_wheel and {self.doors} doors")
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year,crank, helmet, gloves): #hay que poner lo atributos del padre en el init
        self.crank = crank
        self.helmet = helmet
        self.gloves = gloves
        super().__init__(brand, year)
        
    def get_info(self):
        return (f"This motorcycle was made in the year: {self._year}, and the brand is: {self._brand}. This motorcycle uses a {self.helmet} and {self.gloves}")
        
        
car_1 = Car("Kia", 2011, "standart", 4)
print('This car:', car_1.get_info())

motorcycle_1 = Motorcycle("Pulsar", 2023, 1, 1, 2)
print('This motorcycle: ', motorcycle_1.get_info())

