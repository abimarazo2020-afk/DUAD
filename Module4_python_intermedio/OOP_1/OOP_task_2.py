'''EJERCICIO#2
Cree una clase de Bus con:
Un atributo de max_passengers.
Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
Un método para bajar pasajeros uno por uno (en cualquier orden'''


class Person:
    def __init__(self, name):
        self.name = name #aqui se guarda el nombre del objecto
        

class Bus:
    def __init__(self, max_passengers):
        self.passenger_list = [] #Ya no se tiene que pasar como parametro en los demas metodos, solo se llama con self
        self.max_passengers = max_passengers #se guarda la capacidad maxima del bus
        
    def add_passengers(self, person):
        if len(self.passenger_list) < self.max_passengers: #len porque no se puede comparar una lista con un numero.
            self.passenger_list.append(person)
        
        else:
            print("The bus is full we can't add more passengers")
            
    def remove_passenger(self, person):
        if person in self.passenger_list:
            self.passenger_list.remove(person)
        else: 
            print('Passenger not found')
            
def main():
    person_1 = Person("Abigail")
    person_2 = Person("Andres")
    person_3 = Person("Oscar")

    bus_1 = Bus(5)
    bus_1.add_passengers(person_1)
    bus_1.add_passengers(person_2)
    bus_1.add_passengers(person_3)

if __name__ == "__main__":
    main()


# Siempre usa el objeto (bus_1) para llamar métodos
# No la clase (Bus) directamente