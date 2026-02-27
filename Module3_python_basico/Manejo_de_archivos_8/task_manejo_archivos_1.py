'''EJERCICIO#1
Create a program that reads song names from a file (line by line) 
and saves the same names in alphabetical order to another file.'''


def open_songs_file(path):
    list_one = []
    with open(path) as file: #se abre en modo lectura automaticamente, with lo cierra auto
        for song in file.readlines():
            list_one.append(song.strip()) #mientras las leemos las guardamos en la lista, strip quita \n
        new_list = sorted(list_one)

    return new_list


def write_songs(file_path, new_list):
    with open(file_path, 'w') as file:
        for song in new_list:
            file.write(song + '\n')


songs = open_songs_file('songs.txt')
write_songs('sorted_songs.txt', songs)
print(songs)