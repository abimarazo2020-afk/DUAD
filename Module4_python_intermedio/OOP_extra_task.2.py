'''EJERCICIO# 2
Cree una clase base Animal y dos clases hijas Dog y Cat:
Animal debe tener nombre y método speak() que retorne "Hace un sonido"
Dog debe sobrescribir speak() para decir "Guau"
Cat debe sobrescribir speak() para decir "Miau"'''

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return 'Make a sound'
        
    

class Dog(Animal):
    def speak(self):
        return 'guau'
    
class Cat(Animal):
    def speak(self):
        return 'miau'
        
def main():

    dog_1 = Dog('Fofo') #Aqui asignamos name que viene del constructor
    cat_1 = Cat('Venus') ##Aqui asignamos name que viene del constructor

    print(dog_1.speak()) #Aqui llamamos los metodos     
    print(cat_1.speak())
    
if __name__ == "__main__":
    main()