'''EJERICICIO#1
Create a program that reads a text file line by line, excluding line breaks (\n), 
and writes the entire content into a single line in a new file.
'''

def read_file_function(path):
    new_text = ''
    with open(path) as file:
      for line in file.readlines():
        new_text += line.strip() + " "   #esto ultimo agrega un espacio entre palabras, strip quita \n 
        
    with open('output.txt', 'w') as new_file:
       new_file.write(new_text)

    return new_text

last_text = read_file_function('text.txt') #esto no se ocuparia si usamos otra funcion
print(last_text)   




'''EJERICICIO#2
Create a program that opens a text file and counts how many words it contains in total.'''

def open_text_file(path):
    counter = 0
    with open(path) as file:
       for line in file:
          counter += len(line.split()) #la funcion split separa el string en varias palabras 

    return counter
        
total = open_text_file('text.txt')
print(f"Este archivo tiene '{total}' palabras")
          


'''EJERCICIO#3
Create a program that:
Reads a file line by line
Converts each line to uppercase
Writes the contents to a new file'''          

def open_and_read_file(path):
   text_to_convert = ''
   with open(path) as file:
      for line in file.readlines():
         text_to_convert += line.upper()


   with open('converted.txt', 'w') as new_file:
        new_file.write(text_to_convert)

        return text_to_convert
   
result = open_and_read_file('text.txt')
print(result)


'''EJERCICIO#4
Create a program that:
Prompts the user for a line of text
Appends that line to the end of an existing file
If the file does not exist, creates it automatically'''

def enter_your_string():
   text_to_enter = input('enter your text:')
   with open('existing_file', 'a') as file:
      file.write(text_to_enter)

   return text_to_enter

enter_your_string()

