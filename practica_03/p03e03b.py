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
E - Luego imprimir el ranking de los 10 mejores puntajes.
Nota: utilizar una expresión lambda para ordenar el diccionario
"""

#usando diccionario de diccionarios
jugadores = {
    'fede': {'nivel': 3, 'puntaje': 4, 'tiempo': 200}, 
    'belen': {'nivel': 5, 'puntaje': 10, 'tiempo': 400}, 
    'juan': {'nivel': 15, 'puntaje': 110, 'tiempo': 400}, 
    'pedro': {'nivel': 5, 'puntaje': 3, 'tiempo': 400}
}

#A
buscado = 'pedro'
print("Imprimir los datos del jugador buscado: ")
print(jugadores[buscado] if buscado in jugadores else 'El usuario no existe')
print()

#B
print("Nombres de los usuarios que jugaron sin recorrer la estructura:")
print(list(filter(lambda d:jugadores[d]['tiempo'] != 0, jugadores)))
print()

#C
print('Jugador con el mayor puntaje: ')
print(max(jugadores.items(), key=lambda x: x[1]['puntaje']))
print()

#D
partida_nom = input('Ingrese el nombre del Jugador: ')
partida_puntaje = input('Ingrese el puntaje de la jugada de {}: '.format(partida_nom))
if partida_nom in jugadores.keys():
    buscado = jugadores[partida_nom]
    buscado['puntaje'] = max(buscado['puntaje'], int(partida_puntaje))
else:
    print()
    print('El Jugador no existe')

#E
jugadores_ord = sorted(jugadores.items(), key=lambda punt: punt[1]['puntaje'], reverse=True)
print('Ranking TOP 10')
print(jugadores_ord[:10])