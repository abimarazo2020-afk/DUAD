""" 
1-Dada n cantidad de notas de un estudiante, calcular:
-Cuantas notas tiene aprobadas (mayor o igual a 70).
-Cuantas notas tiene desaprobadas (menor a 70).
-El promedio de todas.
-El promedio de las aprobadas.
-El promedio de las desaprobadas. """

1 >  incio

2 > Definir cantidad_de_notas

3 > Definir nota   #nota es un valor que se va a ir sobreescribiendo 

4 > Definir contador_notas 

5 > Definir contador_notas_aprobadas

6 > Definir contador_notas_desaprobadas

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


7 Mostrar "ingrese su cantidad de notas"

8 > pedir cantidad_de_notas

9 > contador_notas = 1

10 > cantidad_de_aprobadas = 0 #contador de aprobadas

11 > cantidad_de_desaprobadas = 0 #contador de desaprobadas

12 > Mientras que (contador < cantidad_de_notas) hacer: 

    a > Mostrar "Ingrese la nota mumero: "

    b > Mostrar contador

    c > pedir nota

    d > Si(nota >= 70 )entonces:

         a > cantidad_de_aprobadas = cantidad_de_aprobadas + 1
  
    e > Sino:

        a > cantidad_de_desaprobadas = cantidad_de_desaprobadas + 1

    f > FinSi

    g > contador = contador + 1

FinMientras

#Recordemos que este ciclo se va a repetir mientras contador sea menor a la cantidad de notas


""" Primer Output 
Cantidad de notas ponemos 3 
contador es 1
cantidad de aprobadas 0
cantidad de desaprobadas 0
en la condicion se cumple porque contador es menos que la cantidad de notas que son 3
como se cumple va a pedir "ingrese la nota numero" + contador
Digamos que se pone un 75 
como la nota es mayor de 70 se cumple esa condicion y la cantidad de aprobadas pasan a ser 1
No tenemos que entrar en el sino, porque la condicion se cumplio
Y aqui agarramos el contador y lo subimos a 2, recordemos que el condigo se va a repetir hasta que se deje
 de cumplir la condicion.
 """

""" Segundo output >> contador = 2
contador = 2
cantidad de aprobadas = 1
cantidad de desaprobadas = 0
vamos a ingresar "ingrese la nota numero" + contador
deberia de mostrar ingrese la nota numero 2
Vamos a ingresar la nota 50 
Aqui la nota no es mayor que 50 asi que se va a cumplir el sino de la condicion del ciclo
la cantidad de desaprobadas ahora seria 1 
termina la condicion y le sumamos al contador. contador + 1
"""

""" Tercer output >> contador = 3
Contador = 3
cantidad de aprobadas = 1
cantidad de desaprobadas = 1
vamos a ingresar "ingrese la nota numero" + contador 
Se va a mostrar el contador en 3.
Ya aqui no se cumpliria la condicion ya que contador seria igual a la cantidad_de_notas.
pero si camiamos la condicion podemos solicitar las 3 notas que el usuario solicito.
Mientras que (contador < cantidad_de_notas) hacer:  >>>>> Mientras que (contador <= cantidad_de_notas) hacer: 
Se le cambia de > a lo siguiente >= donde se prefunta si el contador es menor o igual a la cantidad de notas
esto haria que la condicion se pueda cumplir porque el contador seria igual que la cantidad_de_notas.
ahora vamos a ingresar la nota con un valor de 100
Como 100 es > que 70 se cumpliria que la  cantidad_de_aprobadas aumente 1 y ahora sea 2.
El contador aumenta + 1  
cantidad_de_aprobadas + 1
 """

""" Cuarto output >> contador 4 
Contador = 4
cantidad_de_aprobadas = 2
vamos a ingresar "ingrese la nota numero" + contador 
Se va a mostrar el contador en 4.
Ya aqui no se va a cumplir la condicion porque el contador no es menor ni igual que la cantidad_de_notas.

"""
+++++++++++++++++++++++ ~~~~~~~~~~~~~~~~~~~~~~~~~~ ++++++++++++++++++++++++ ~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" Ya con todo esto tenemos la logica del programa lista solo faltaria sacar los promedios """


1 >  incio

2 > Definir cantidad_de_notas

3 > Definir nota   #nota es un valor que se va a ir sobreescribiendo 

4 > Definir contador_notas 

5 > Definir contador_notas_aprobadas

6 > Definir contador_notas_desaprobadas

7 > Definir promedio_total

8 > Definir promedio_aprobadas

9 > Definir promedio_desaprobadas


"""  Un promedio es cuando se agarra una cantidad de numeros los suma y los divide entre esa cantidad 
eso haria que para sacar este promedio ocupa agarrar la cantidad_de_notas y dividirlas entre 3 """

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


10 Mostrar "ingrese su cantidad de notas"

11 > pedir cantidad_de_notas > 3

12 > contador_notas = 1 >>  4

13 > cantidad_de_aprobadas = 0 >> 2 #contador de aprobadas

14 > cantidad_de_desaprobadas = 0 >> 1 #contador de desaprobadas

15 > pomedio_total = 0 → 75 + 50 + 100 = 225 / 3 = 75

16 > promedio_aprobadas = 0 → 75 + 100 / 2 = 87.5

17 > promedio_desaprobadas = 0 → 50 / 1 = 50

18 > Mientras que (contador < cantidad_de_notas) hacer: 

    1 > Mostrar "Ingrese la nota mumero: "

    2 > Mostrar contador

    3 > pedir nota

    4 > Si(nota >= 70 )entonces:

         1 > cantidad_de_aprobadas = cantidad_de_aprobadas + 1
         2 > promedio_aprobadas = promedio_aprobadas + nota
  
    5 > Sino:

         1 > cantidad_de_desaprobadas = cantidad_de_desaprobadas + 1
         2 > promedio_desaprobadas = promedio_desaprobadas + nota

    6 > FinSi

    7 > promedio_total = promedio_total + nota # entre la cantidad de notas osea 3 

    8 > contador = contador + 1

19 FinMientras

20 > promedio_total = promedio_total / cantidad_de_notas  
#Notese que aqui no se puede devidir entre la cantidad de notas porque siempre seria 3.
#ya que ese es el valor de la variable cantidad_de_notas.
21 > promedio_aprobadas = promedio_aprobadas / cantidad_de_aprobadas  

22 > promedio_desaprobadas = promedio_desaprobadas / cantidad_de_desaprobadas 

23 Mostrar 'Su cantidad de notas aprobadas fue:'

24 > Mostrar cantidad_aprobadas

25 > Mostrar 'Su cantidad de notas desaprobadas fue:'

26 > Mostrar cantidad_de_desaprobadas 

27 > Mostar 'su promedio_total fue': 

28 > Mostar Promedio_total

29 > Mostrar 'Su promedio_aprobadas fue:'

30 > Mostar promedio_aprobadas

31 > 'Mostar promedio_desaprobadas fue:'

32 > Mostar promedio_desaprobadas

33 > FinMientras

