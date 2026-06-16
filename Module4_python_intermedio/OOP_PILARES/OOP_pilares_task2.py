'''Cree una clase abstracta de Shape que:
Tenga los métodos abstractos de calculate_perimeter y calculate_area.
Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.'''

from abc import ABC, abstractmethod #IMPORTANTE

#CLASE PADRE
class Shape(ABC):
    
    @abstractmethod 
    def calculate_perimeter(self):
        pass
        
    @abstractmethod
    def calculate_area(self):
        pass
        
#CLASE HIJA 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    
    def calculate_perimeter(self):
       pi = 3.14
       return 2 * pi * self.radius
        
    def calculate_area(self):
        pi = 3.14
        return pi * self.radius ** 2
        
        
#CLASE HIJA
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_perimeter(self):
        return 4 * self.side
        
    def calculate_area(self):
        return self.side ** 2
        


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
        
    def calculate_area(self):
        return self.width  * self.height
        
        
        
    
def main():
    
    #CREACION OBJECTO CIRCLE
    radius = float(input('Enter your radius: '))
    
    circle_1 = Circle(radius)
    
    print('circle_1 perimeter: ', circle_1.calculate_perimeter())
    
    print('circle_1 area: ', circle_1.calculate_area())
    
    
    
    #CREACION OBJECTO SQUARE
    side = float(input('Enter the size of your side: '))
    
    square_1 = Square(side)
    
    print('square_1 permiter: ', square_1.calculate_perimeter())
    
    print('square_area: ', square_1.calculate_area())
    
    
    #CREACION OBJECTO RECTANGLE
    width = float(input('Enter your rectangle width: '))
    height = float(input('Enter your rectangle height: '))
    
    rectangle_1 = Rectangle(width, height)
    
    print('rectangle_1 perimeter: ', rectangle_1.calculate_perimeter())
    
    print('rectangle_1 area: ', rectangle_1.calculate_area())


    