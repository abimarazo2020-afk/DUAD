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



'''EJERCICIO#2
Read about the other methods in the csv module here 
and create an alternative version of the exercise above that saves the file separated by tabs instead of commas.
'''

import csv

def input_game_information():
	name = input('Enter the game name: ')
	genre = input('Enter the genre: ')
	developer = input('Enter the developer name: ')
	esrb_rating = input('Enter the ESRB rating: ')

	game_dic = {
		'Name': name,
		'Genre': genre,
		'Developer': developer,
		'ESRB Rating': esrb_rating
	}

	return game_dic


def write_tsv_file(file_path, games_list):
	headers = ['Name', 'Genre', 'Developer', 'ESRB Rating']

	with open(file_path, 'w', newline='', encoding='utf-8') as file:
		writer = csv.DictWriter(
			file,
			fieldnames=headers,
			delimiter='\t'   # tabulaciones
		)
		writer.writeheader()
		writer.writerows(games_list)





def main():
	games_list = []
	while True:
		game = input_game_information()
		games_list.append(game)
		
		another = input('Add another game? (y/n): ')
		if another.lower() != 'y':
			break

	write_tsv_file('games.tsv', games_list) #cambia de cvs a tsv


if __name__ == "__main__":
	main()
