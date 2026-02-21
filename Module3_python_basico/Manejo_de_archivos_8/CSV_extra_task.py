'''Ejercicio#1
Create a program that opens a .csv file containing video game information 
(the one generated in exercise 1) and:
Reads each line using csv.reader()
Displays the contents on the screen in a readable way, line by line'''

import csv

def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file) 
        for row in reader:
            print(row)

read_csv_file('games.csv')

#reader = csv.reader(file)  otro metodo para leer el csv file, este lee como si fuera lista
#el orden importa y tambien de esta forma no usa nombres de columnas.


'''EJERCICIO#2
Create a program that opens a .csv file containing video game information (based on the CSV file generated in exercise 1) and:
Reads the video game CSV file
Asks the user for an ESRB rating (for example: "T")
Displays all video games with that rating'''

import csv

def open_and_read_csv(file_path):
    user_esrb = input('Enter your esrb: ')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if user_esrb == row['ESRB Rating']:
                print(row)
                           
            

open_and_read_csv('games.csv')



'''EJERCICIO#3
Create a program that opens a .csv file containing video game information 
(based on the CSV file generated in exercise 1) and:
Reads the .csv file containing video games
Counts how many video games there are in each genre
Displays the results in an organized manner'''

import csv

def open_and_read_csv(file_path):
    action_counter = 0
    adventure_counter = 0
    sandbox_counter = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Genre'] == "Action":
                action_counter += 1
            elif row['Genre'] == "Adventure":
                adventure_counter += 1
            elif row['Genre'] == "Sandbox":
                  sandbox_counter += 1

    print("Cantidad de videojuegos por género:")
    print("Action:", action_counter)
    print("Adventure:", adventure_counter)
    print("Sandbox:", sandbox_counter)

open_and_read_csv("games.csv")




'''EJERCICIO#4
Create a program that opens a .csv file containing video game information
 (based on the CSV file generated in exercise 1) and:
Reads the .csv file containing video games
Asks the user to enter the name of a developer (e.g., "Ubisoft")
Displays all video games developed by that company in a readable format:'''

import csv

def open_and_read_csv(file_path):
    developer_name = input('Enter your developer name: ')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if developer_name == row['Developer']:
                print('Game:', row['Name'])
                print('Developer:', row['Developer'])

open_and_read_csv('games.csv')


