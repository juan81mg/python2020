"""
3. Para registrar las actividades de un usuario en un juego dado se requiere guardar los siguientes
datos: nombre del jugador, nivel alcanzado en el juego, puntaje máximo y tiempo de juego.
Realizar los siguientes items con esta estructura:
- Seleccione la estructura que considere más adecuada para almacenar la información de
varios usuarios ingresados desde teclado. Tener en cuenta que se necesita acceder a un
usuario determinado en forma directa sin recorrerla.
A - Con la estructura generada, imprimir los datos de un usuario dado sin recorrer la estructura.
¿La elección sobre la estructura fue adecuada? ¿Cuál usó?
B - Con la estructura generada en el ejercicio, imprimir sólo los nombres de los usuarios que
jugaron sin recorrer la estructura.
C - Dada la estructura generada en el ejercicio imprimir el usuario que obtuvo mayor puntaje.
D - Dada la estructura del ejercicio, ingresar los datos correspondientes a la jugada de un
usuario. Si el usuario existe previamente, guardar los datos de mayor puntaje.
Luego imprimir el ranking de los 10 mejores puntajes.
Nota: utilizar una expresión lambda para ordenar el diccionario
"""

#usando diccionario de diccionarios
jugadores = {'fede': { 'nivel': 3, 'puntaje': 4, 'tiempo': 200 }, 'belen': { 'nivel': 5, 'puntaje': 10, 'tiempo': 400 }, 'juan': { 'nivel': 15, 'puntaje': 110, 'tiempo': 400 }, 'pedro': { 'nivel': 5, 'puntaje': 3, 'tiempo': 400 }}
print(jugadores)
#A
print(jugadores['pedro'])
#B
print(jugadores.keys())

print('='*55)

#todos los datos
print(jugadores.items())

#recorro la estructura
for jugador in jugadores.items():
    print(jugador)

#recorro y accedo al nombre de cada jugador
for jugador in jugadores.items():
    print(jugador[0])

#recorro y accedo al nombre de cada jugador por nivel
for jugador in jugadores.items():
    print(jugador[1]['nivel'])

#accedo a todos los datos del jugador
for jugador in jugadores.items():
    print('El jugador {} tiene los siguientes datos:'.format(jugador[0]))
    for dato in jugador[1].keys():
        print('En {} es: {}'.format(dato, jugador[1][dato]))

