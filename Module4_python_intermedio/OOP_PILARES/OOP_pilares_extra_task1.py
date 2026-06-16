'''Cree una clase Employee con los siguientes requisitos:
Atributos privados: _name, _salary
Use @property y @<atributo>.setter para:
Mostrar el nombre y el salario
Validar que el salario nunca sea negativo
Cree un método promote que aumente el salario un porcentaje definido'''

class Employee:
    def __init__(self, name, salary):
        self.__name = name #aqui no llama a setter
        self.salary = salary #aqui llama a setter 
        
    #Metodo con @property
    @property
    def name(self):
        return self.__name
        
    @property            #un property por atributo
    def salary(self):
        return self.__salary
        
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("The value can't be negative")
        else:
            self.__salary = value #aqui lo guarda como atributo
            
    def promote_salary(self, percentage):
        self.salary = self.salary * (1 + percentage)
        
#Creacion de objectos con property
employee_1 = Employee('Abigail', 2700)
print(employee_1.name) #Abigail
print(employee_1.salary) #2700

employee_1.salary = 3000
print(employee_1.salary) #3000

employee_1.salary = -500 #error porque es negativo el valor que se asigna

#usamos metodo promote
employee_1.promote_salary(0.10)   # +10%
print(employee_1.salary)


        
        
#Aqui name queda solo con property y no con setter:
 
#  Porque:

# ✔ Solo lo quieres leer
# ❌ No necesitas validarlo
# ❌ No necesitas cambiarlo después
        
        
#METODO SIN @property
# employee_1 = Employee("Abigail") #aqui es publico pero luego se guarda en __name
# print(employee_1.get_name()) # 👈 llamas función





#Este codigo guarda los atributos name y salary sin validarlos y sin setter 
# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name #atributo privado > python trasnforma esto a self._Employee__name
#         self.__salary = salary #atributo privado > python transforma esto a self.Employee__salary
        
#     #Metodo con @property
#     @property
#     def name(self):
#         return self.__name
        
#     @property            #un property por atributo
#     def salary(self):
#         return self.__salary
        
#     @salary.setter
#     def salary(self, value):
#         print('setter working: ')
#         self.__salary = value
        
# #Creacion de objectos con property
# employee_1 = Employee('Abigail', 2700)
# print(employee_1.name)
# print(employee_1.salary)



        

        
        
        
        
    
    