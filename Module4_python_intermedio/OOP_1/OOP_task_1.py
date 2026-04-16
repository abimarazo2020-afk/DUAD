'''EJERCICIO#1
Cree una clase de Circle con:
Un atributo de radius (radio).
Un método de get_area que retorne su área.
'''

class Circle:
   def __init__(self, radius):
     self.radius = radius
   
   def get_area(self):
     pi = 3.14 #como pi vale lo mismo siempre no se pone como parametro despues de self, se define adentro
     formula = (self.radius * self.radius) * pi 
     print(f'the area of the circle is {formula}')
     return formula
     
my_circle = Circle(30)
my_circle.get_area()
     

   
   
   
   