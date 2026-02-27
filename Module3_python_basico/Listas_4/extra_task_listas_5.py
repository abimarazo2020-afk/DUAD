'''EJERCICIO#5
Create a program that asks the user to enter 5 words. 
Then display a new list with only those words that have more than 4 letters.'''

words_counter = 1
list_five = []
new_list_five = []

while words_counter <= 5:
    words = str(input(f'Enter your word {words_counter}:'))
    list_five.append(words)
    words_counter += 1


for word in list_five:
    if len(word) > 4:
        new_list_five.append(word)

print(new_list_five)
