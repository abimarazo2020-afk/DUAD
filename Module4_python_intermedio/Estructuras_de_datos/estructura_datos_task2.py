'''EJERCICIO#2
Cree una estructura de objetos que asemeje un Double Ended Queue.
Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y
pop_right (para quitar nodos al inicio y al final).
Debe incluir un método para hacer print de toda la estructura.
No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.before = None #no van como paramtros Porque normalmente esos enlaces (siguiente y anterior) todavía no existen cuando el nodo se crea
        self.next = None #aun no se sabe quien es quien por eso
        
        
        
class Deque:
    def __init__(self):
        self.head = None
        self.final = None
        
    def push_right(self, data):
    
        node_1 = Node(data) #se crea el node 
        
        #Insertar al final #aqui apunta el primer nodo al head y al final
        if self.final is None:
            self.head = node_1
            self.final = node_1
        
        else:
            node_1.before = self.final
            self.final.next = node_1
            
            self.final = node_1
            
    def push_left(self, data):
        
        node_1 = Node(data)
        
        #insertar al inicio
        if self.head is None:
            self.head = node_1
            self.final = node_1
            
        else: 
            node_1.next = self.head
            self.head.before = node_1
            
            #vovlveamos a asignar head
            self.head = node_1 ## el nuevo nodo ahora es el inicio
            
            
    def print_estructure(self):
        temp = self.head
        while temp:
            print(temp.data, end = "-")
            temp = temp.next
            
        print()
        
        
    def pop_right(self):
        
        if not self.final:
            return None
            
        temp_final = self.final
        
        if self.final == self.head:
            self.head = None
            self.final = None
            
        else:
            self.final = self.final.before
            self.final.next = None
        return temp_final.data
            
    def pop_left(self):
    
        if not self.head: #si no existe head retorne None
            return None 
            
        temp_head = self.head #guardamos la cabeza
        
        #si solo hay un nodo:
        if self.head == self.final:
            self.head = None
            self.final = None
            
        else:
            self.head = self.head.next
            self.head.before = None
        return temp_head.data
        
        
#frente -> [5] <-> [10] <-> [20] <- final

#CREACION DE OBJECTOS:
deque = Deque()

deque.push_right(30)
deque.print_estructure()

deque.push_right(20)
deque.print_estructure()

deque.push_left(10)
deque.print_estructure()

deque.push_left(5)
deque.print_estructure()

deque.pop_left()
deque.print_estructure()

deque.pop_right()
deque.print_estructure()


#OUTPUT DEL CODIGO:

# 30-
# 30-20-
# 10-30-20-
# 5-10-30-20-
# 10-30-20-
# 10-30-