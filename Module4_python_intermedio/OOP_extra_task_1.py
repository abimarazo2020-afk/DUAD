'''EJERCICIO#1
Cree una clase Rectangle que:
Tenga atributos width y height
Tenga un método get_area() que retorne el área
Tenga un método get_perimeter() que retorne el perímetro
Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado'''


class Rectangle:
    def __init__(self, width, height):
        if self.width < 0 or self.height < 0: #solo parametros, no se han guardado
            raise ValueError('The width and height cant be negatives numbers')
             
        self.width = width #guardamos el atributo
        self.height = height
        
    def get_area(self): #formula ancho/base * altura
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * (self.width + self.height)
        
        
# CREACION DE OBJECTOS

def main():
    width = float(input('Enter the rectangle width: '))
    height = float(input('Enter the rectangle height: '))
    
    rectangle_1 = Rectangle(width, height) #aqui asignamos los inputs y los inputs a los parametros de la clase
      
    print("Area", rectangle_1.get_area())
    print("perimeter", rectangle_1.get_perimeter())
    
if __name__ == "__main__":
    main()
        
    
