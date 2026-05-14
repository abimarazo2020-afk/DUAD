'''                               ESTRUCTURAS DE DATOS                           '''

'''LINKED LIST'''

#Para crear un linked list se ocupa la clase del nodo y la clase del linked list
#la linked list una estructura que tiene un atributo head que referencia a su primer elemento o nodo
#la clase nodo tiene un valor y un atributo next que se setea como none al principio

#class linked list:
class LinkedList:
	def __init__(self, head):
		self.head = head


#Asi se ve la estructura con los dos:
class Node:
  data: str  #son hints no variables
  next: "Node" #son hints no variables 

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head
		
		
'''El atributo data va a tener cualquier valor que queramos en el nodo. En este caso, crearemos una LinkedList de strings, así que el data de cada nodo será un string.
Perfecto, ahora podemos crear una Linked List con algunos nodos.'''

class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)

# En este caso, el third_node será el último nodo.
# El second_node será el del medio y su next será el third_node.
# El first_node será el head de linked_list y su next será el second_node.



'''Ahora necesitamos una manera de printear sus nodos para saber que está funcionando correctamente.
Lo primero que necesitamos es tomar el primer nodo, y sabemos que es el head.
Teniendo ese head, podemos hacer print de su data.'''


class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head
    print(current_node.data)


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()


'''Perfecto, ahora si quisieramos hacer print del segundo nodo también,
tenemos que accesarlo usando el next del primero (que ya tenemos guardado en la variable current_node).'''

class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head
    print(current_node.data)

    current_node = current_node.next
    print(current_node.data)


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()



'''A pesar de que esto va muy bien, no podemos seguir haciendolo con código estático.
No funcionaría con estructuras de distintas cantidades de nodos.
Sin embargo, si ponemos atención, verémos que ya tenemos un patrón que podemos enciclar.'''


class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head
    print(current_node.data)

    current_node = current_node.next
    print(current_node.data)

    current_node = current_node.next
    print(current_node.data)


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()



# Lo que tenemos que hacer es seguir sobreescribiendo el valor del current_node por su next y printeando su data, 
# siempre y cuando este no sea None.
# Si llegamos al None, significa que ya pasamos el ultimo nodo de la lista, cuyo next era ese None.
# Esto lo podemos lograr con un while (ya que no tenemos certeza de cuantas veces debe correr, pero sí de cuando tiene que parar).

class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head

    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()






'''           CREANDO UN QUEUE                      '''

class Node:
  data: str

  def __init__(self, data, next=None): #None Porque normalmente al crearlo todavía no apunta a nadie.
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
        
    def print_structure(self): 
        current_node = self.head

        while current_node is not None: #Recorre toda la lista e imprime nodo por nodo.
            print(current_node.data)
            current_node = current_node.next

class Queue(LinkedList): #Aquí tu Queue hereda de LinkedList.
  def enqueue(self, new_node): #Esto agrega un nodo al FINAL de la cola.
    current_node = self.head #Empieza desde el primer nodo.
    next_node = current_node.next #uarda el siguiente nodo.
    while (next_node is not None): #“Mientras exista otro nodo… “Mientras NO lleguemos al final.”
      current_node = next_node #avanza
      next_node = current_node.next #apunta al siguiente 

#cuando se llegue a none se sale del while y pasa lo siguiente:
    current_node.next = new_node #agrega el nuevo

  def dequeue(self): #Esto quita el PRIMER nodo.
    self.head = self.head.next  #ESTA LÍNEA ES LA MÁS IMPORTANTE  Mueve el head al siguiente nodo. y lo elimina


tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)

queue = Queue(primer_nodo) #La cola empieza desde primer_nodo.

print("Agregando un elemento")

queue.enqueue(Node("Soy el nuevo nodo!")) #Crea un nodo nuevo y lo agrega al final. 

# Antes:

# primer -> segundo -> tercero

# Después:

# primer -> segundo -> tercero -> nuevo

queue.print_structure()


print("Quitando un elemento")

queue.dequeue() #Quita el primero.

queue.dequeue()

# Quita el primero.

# Antes:

# primer -> segundo -> tercero -> nuevo

# Después:

# segundo -> tercero -> nuevo

queue.print_structure()


#estructura completa 

# Node
#  ↓
# crea nodos

# LinkedList
#  ↓
# guarda head y métodos generales

# Queue
#  ↓
# usa LinkedList
# y agrega enqueue/dequeue