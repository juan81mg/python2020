"""2. 
2A - Registrar los jugadores del Ejercicio 3 de la Práctica 3 en un archivo
utilizando cualquiera de las librerías dadas en la teoría (Pickle, JSON,
CSV). 

2B - Implementar una función denominada modificoDatos, la cual solicita 
(mediante una interfaz generada con PySimpleGUI) los datos de un
jugador, si este existe en el archivo, modifica dichos datos en el mismo.
Si no existe el jugador, lo agrega."""


import json

#2A
def guardoDatos(jugadores):
    archivo = open('p04e02_Partidas.dat', 'w')
    json.dump(jugadores, archivo)
    archivo.close()

#2B
def modificoDatos():
    pass

#datos - usando diccionario de diccionarios
jugadores = {
    'fede': {'nivel': 3, 'puntaje': 4, 'tiempo': 200}, 
    'belen': {'nivel': 5, 'puntaje': 10, 'tiempo': 400}, 
    'juan': {'nivel': 15, 'puntaje': 110, 'tiempo': 400}, 
    'pedro': {'nivel': 5, 'puntaje': 3, 'tiempo': 400}
}

#A - devuelve los datos de un jugador ne particular
buscado = 'pedro'
print("Imprimir los datos del jugador buscado: ")
print(jugadores[buscado] if buscado in jugadores else 'El usuario no existe')
print()

#B - jugadores que jugaron, sin recorrer la estructura
print("Nombres de los usuarios que jugaron sin recorrer la estructura:")
print(list(filter(lambda d:jugadores[d]['tiempo'] != 0, jugadores)))
print()

#C - devuelve el jugador con mayor puntaje
print('Jugador con el mayor puntaje: ')
print(max(jugadores.items(), key=lambda x: x[1]['puntaje']))
print()

#D - actualiza una partida si existe el jugador
partida_nom = input('Ingrese el nombre del Jugador: ')
partida_puntaje = input('Ingrese el puntaje de la jugada de {}: '.format(partida_nom))
if partida_nom in jugadores.keys():
    buscado = jugadores[partida_nom]
    buscado['puntaje'] = max(buscado['puntaje'], int(partida_puntaje))
else:
    print()
    print('El Jugador no existe')

#E - ranking top 10
jugadores_ord = sorted(jugadores.items(), key=lambda punt: punt[1]['puntaje'], reverse=True)
print('Ranking TOP 10')
print(jugadores_ord[:10])

guardoDatos(jugadores)