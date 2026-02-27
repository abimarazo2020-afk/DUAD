''''EJERCICIO#2
Create a function that takes a list of words and a number n,
 and returns a new list with only the words that have more than n letters.
'''

def return_new_list_function(words_list, n):
    new_list = []
    for word in words_list:
        if len(word) >= n:
            new_list.append(word)

    return new_list

print(return_new_list_function(['Buenas', 'Tardes', 'Companeros'], 3))