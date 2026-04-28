'''Cree las siguientes clases:
Head
Torso
Arm
Hand
Leg
Feet
Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.'''

class Head:
    def __init__(self):
        pass
    

class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm

        
    
    
class Arm:
    def __init__(self, hand):
        self.hand = hand
    

    
class Hand:
    def __init__(self):
        pass
      
    

class Leg:
    def __init__(self, foot):
        self.foot = foot
        
        
    
    
class Foot:
    def __init__(self):
        pass
        
    

class Human:
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg


#CREACION DE OBJECTOS:

def main():
    head = Head() #aqui se crea el objecto head

    left_hand = Hand() #aqui se crea el objecto mano
    right_hand = Hand()

    right_arm = Arm(right_hand) #aqui se crea el objecto brazo entero con los objectos hand adentro
    left_arm = Arm(left_hand)

    torso = Torso(head, right_arm, left_arm) #aqui se crea el objecto torso con los objectos brazos dentro

    right_foot = Foot() #aqui se crea el objecto pie
    left_foot = Foot()

    left_leg = Leg(left_foot) #aqui se crea el objecto pierna con el objecto pie dentro 
    right_leg = Leg(right_foot)

    human = Human(torso, right_leg, left_leg)





#COMPOSICION
#  Arm → Hand
#  Leg → Foot
#  Torso → Head + Arms
#  Human → Torso + Legs
#Sin duplicados y cosas inecesarias