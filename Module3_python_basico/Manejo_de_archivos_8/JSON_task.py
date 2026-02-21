'''EJERCICIO#
Create a program that allows you to add a new Pokémon to the JSON lesson file.
You must read the file to import the existing Pokémon.
Then you must request the information for the Pokémon to be added.
Finally, you must save the new Pokémon to the file.
'''

import json


def read_open_file(path): #path viene desde main() como pokemons.json
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)





#el archivo json empieza con una lista, no con un diccionario, eso significa que para agregar pokemons
#se le agregan a la lista no al dic

def enter_pokemon_information(): #no se usa paramatro porque la info que se ocupa se pide adentro
    types = [] #en el json file, type es una lista ojo.

    pokemon_name = input('Enter your pokemon name: ')
    Level = int(input('Enter the pokemon level: '))

    while True:  #while true porque no se cuantos se van a ingresar
        type = input('Enter your pokemon types or press enter to finish:')
        if type == '':
            break
        types.append(type)
        


    hp = int(input('Enter your pokemon HP: '))
    attack = int(input('Enter your attack: '))
    defense = int(input('Enter your defense: '))
    sp_attack = int(input('Enter your sp.attack: '))
    sp_defense = int(input('Enter your sp.defense: '))
    speed = int(input('Enter your speed: '))

    new_pokemon_dic = {

        'name' : {
            'english': pokemon_name
        },
        'level': Level,
        'type':types,
        
        'base': {
            'HP': hp,
            'Attack': attack,
            'Defense': defense,
            'Sp. Attack': sp_attack,
            'Sp. Defense': sp_defense,
            'Speed': speed
        }
           
    }

    return new_pokemon_dic
        

def main():

    pokemons = read_open_file("pokemons.json") 
    #en esta variable pokemons se guardan los pokemones en memoria, es una lista.

    new_pokemon = enter_pokemon_information()
    #En varaible para poder utilizar el resultado

    pokemons.append(new_pokemon)

    with open('pokemons.json', 'w', encoding='utf-8') as file:        #file representa el archivo abierto
        json.dump(pokemons, file, indent=2)         #aqui dice que guardemos los pokemons en la variable file



if __name__ == "__main__":
    main()
