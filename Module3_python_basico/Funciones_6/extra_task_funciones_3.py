'''EJERCICIO#3
Create a function that takes a string and returns how many vowels it contains.
'''

def vowels_function(My_string):
   vowels = 'aeiouAEIOU'
   contador = 0
   for letter in My_string:
       if letter in vowels:
           contador += 1

   return contador

print(vowels_function('Entendimiento'))