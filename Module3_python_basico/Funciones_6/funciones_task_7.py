'''EJERCICIO#7
Create a function that accepts a list of numbers and returns a list of the prime numbers in that list.

[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Research the mathematical logic for determining if a number is prime and translate it into code. 
Don't look for the code itself; that won't help.

Tip 2: This involves several steps (iterating through the list, checking if each number is prime, and adding it to another list). 
Therefore, it's best to add another function to check if the number is prime or not.
'''


def is_prime(n):
    if n <= 1:
        return False #quita los negativos y menores que 1
        

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True



def prime_numbers_function(list_numbers = [1, 2, 3, 4, 5, 11, 12, 13]):
    primes = []
    for number in list_numbers:
        if is_prime(number):
            primes.append(number)

    return primes