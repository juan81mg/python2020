"""2. 
2A - Registrar los jugadores del Ejercicio 3 de la Práctica 3 en un archivo
utilizando cualquiera de las librerías dadas en la teoría (Pickle, JSON,
CSV). 
2B - Implementar una función denominada modificoDatos, la cual solicita 
(mediante una interfaz generada con PySimpleGUI) los datos de un
jugador, si este existe en el archivo, modifica dichos datos en el mismo.
Si no existe el jugador, lo agrega."""

import json
import PySimpleGUI as sg

#2B
def modificoDatos(jugadores):
    layout = [sg.Text('Nombre', size=(15, 1)), sg.InputText()], [sg.Text('Nivel', size=(15, 1)), sg.InputText()], [sg.Text('Puntaje', size=(15, 1)), sg.InputText()], [sg.Text('Tiempo', size=(15, 1)), sg.InputText()], [sg.OK(), sg.Button('Cancelar')]
    win = sg.Window('Modificar datos:').Layout(layout)
    while True:
        event, values = win.read()
        if event is None or event == 'Cancelar':
            break
        if event == 'OK':
            # si el jugador existe
            if values[0] in jugadores.keys():
                jugadores[values[0]]['nivel'] = values[1]
                jugadores[values[0]]['puntaje'] = values[2]
                jugadores[values[0]]['tiempo'] = values[3]
            else:
                jugadores[values[0]] = {'nivel':values[1],'puntaje':values[2],'tiempo':values[3]}
            win.close()

    return(jugadores)

#2A
def guardoDatos(jugadores):
    archivo = open('p04e02_Partidas.dat', 'w')
    json.dump(jugadores, archivo)
    archivo.close()

#D - actualiza una partida si existe el jugador
def agregar_jugada(jugadores):
    partida_nom = input('Ingrese el nombre del Jugador: ')
    partida_puntaje = input('Ingrese el puntaje de la jugada de {}: '.format(partida_nom))
    if partida_nom in jugadores.keys():
        buscado = jugadores[partida_nom]
        buscado['puntaje'] = max(buscado['puntaje'], int(partida_puntaje))
    else:
        print()
        print('El Jugador no existe')

#C - devuelve el jugador con mayor puntaje
def mayor_puntaje(jugadores):
    print('Jugador con el mayor puntaje: ')
    print(max(jugadores.items(), key=lambda x: x[1]['puntaje']))
    print()

#B - jugadores que jugaron, sin recorrer la estructura
def listar_jug(jugadores):
    print("Nombres de los usuarios que jugaron:")
    print(list(filter(lambda d:jugadores[d]['tiempo'] != 0, jugadores)))
    print()

#A - devuelve los datos de un jugador en particular
def buscar_jug(jugadores):
    buscado = input('Ingrese el nombre del jugador a buscar: ')
    print("Datos del jugador buscado: ")
    print(jugadores[buscado] if buscado in jugadores else 'El usuario no existe')
    print()

#E - ranking top 10
def ranking(jugadores):
    jugadores_ord = sorted(jugadores.items(), key=lambda punt: punt[1]['puntaje'], reverse=True)
    print('Ranking TOP 10')
    print(jugadores_ord[:10])
    print()

#datos - usando diccionario de diccionarios
jugadores = {
    'fede': {'nivel': 3, 'puntaje': 4, 'tiempo': 200}, 
    'belen': {'nivel': 5, 'puntaje': 10, 'tiempo': 400}, 
    'juan': {'nivel': 15, 'puntaje': 110, 'tiempo': 400}, 
    'pedro': {'nivel': 5, 'puntaje': 3, 'tiempo': 400}
}

op = 9
while op != 0:
    op = int(input('1: Modificar un Jugador\n2: Buscar un Jugador\n3: Lista de Jugadores\n4: Jugador con Mayor Puntaje\n5: Agregar Jugada\n6: Ranking 10 Mejores Puntajes\n7: Guardar los Datos\n0: para terminar\n'))
    if op == 1:
        modificoDatos(jugadores)
    elif op == 2:
        buscar_jug(jugadores)
    elif op == 3:
        listar_jug(jugadores)
    elif op == 4:
        mayor_puntaje(jugadores)
    elif op == 5:
        agregar_jugada(jugadores)
    elif op == 6:
        ranking(jugadores)
    elif op == 7:
        guardoDatos(jugadores)

print('<<< FIN >>>\n',)