''''EJERICIO#1
Create a program that iterates through 
and prints the values ​​of two lists of the same size at the same time.'''

first_list = ['today', '26', 'the day is']
second_list = ['is', 'of december', 'cloudy']

if len(first_list) == len(second_list):
    for i in range(len(first_list)):
        print(f'the element of the list 1: {first_list[i]}, element of the 2 list: {second_list[i]}') #poner el indice dentro de la variable hace  que imprima el elemento no el indice

else: 
    print("the lists doesn't match the lenght") 



