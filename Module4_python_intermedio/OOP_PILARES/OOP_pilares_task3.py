'''Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.'''

'''Multifuncional smartphone'''

class Camara:
    def take_picture(self):
        print('Taking picture')
    

class Music:
    def play_music(self):
        print('You are listing Burna boy')
    
    
class Calling:
    def calling(self):
        print('Calling mom')
    
    
class Smartphone(Camara, Music, Calling):
    pass
    
    
smartphone_1 = Smartphone()
smartphone_1.take_picture()
smartphone_1.play_music()
smartphone_1.calling()