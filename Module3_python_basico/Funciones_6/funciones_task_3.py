'''EJERICICIO#3
Create a function that returns the sum of all the numbers in a list.

The function will take one parameter (the list) and return a number (the sum of all its elements).

[4, 6, 2, 29] → 41'''


def function_four(list_one):
    counter = 0
    for number in list_one:
        counter += number

    return counter

print(function_four([1, 2, 3, 4, 5]))