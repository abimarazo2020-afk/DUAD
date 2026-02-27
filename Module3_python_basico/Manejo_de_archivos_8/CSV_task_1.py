'''EJERCICIO#1
Create a program that allows me to input information for any number of video games and saves it to a CSV file.

It must include:
Name
Genre
Developer
ESRB Rating'''

import csv

def input_game_information():
    name = input('Enter the game name: ')
    genre = input('Enter the genre: ')
    developer = input('Enter the developer name: ')
    esrb_rating = input('Enter the esrb rating: ')


    games_dic = {

            
        'Name' : name,
        'Genre' : genre,
        'Developer' : developer,
        'ESRB Rating' : esrb_rating
    
    }
    

    return games_dic



def write_csv_file(file_path, games_list): #file path nos dice donde escribir el archivo y games_list que escribir
    headers = ['Name', 'Genre', 'Developer', 'ESRB Rating']


    with open(file_path, 'w', newline='', encoding='utf-8') as file: #new line elimina lineas en blanco
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(games_list)


def main():
	games_list = [] #la lista va fuera del while porque los valores se ocupan resevar no cambiarlos
	
	while True:
		game = input_game_information()
		games_list.append(game)
		
		another = input('Add another game? (y/n): ')
		if another.lower() != 'y':
			break
		
	write_csv_file('games.csv', games_list)
	print('Games saved to games.csv')

