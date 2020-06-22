"""
Utilizando la solución del ejercicio anterior, se deberá restringir para que
las 5 letras se agreguen al tablero B de forma consecutiva, sea en forma
horizontal y/o vertical.
"""
import PySimpleGUI as sg
from random import randint


def obtener_extremos(limite_extremo_uno_original, limite_extremo_dos_original, nuevo_limite):
    # El límite uno será el que está más a la izquierda o más arriba
    # El límite dos será el que está más a la derecha o más abajo

    if limite_extremo_uno_original[0] < limite_extremo_dos_original[0] \
            and limite_extremo_uno_original[1] == limite_extremo_dos_original[1]:
        # Originalmente el segundo extremo está a la derecha
        # Se mantiene el orden
        limite_extremo_uno = limite_extremo_uno_original
        limite_extremo_dos = limite_extremo_dos_original

    elif limite_extremo_uno_original[0] > limite_extremo_dos_original[0] \
            and limite_extremo_uno_original[1] == limite_extremo_dos_original[1]:
        # Originalmente el segundo extremo está a la izquierda
        # Se invierten los límites
        limite_extremo_uno = limite_extremo_dos_original
        limite_extremo_dos = limite_extremo_uno_original

    elif limite_extremo_uno_original[1] < limite_extremo_dos_original[1] \
            and limite_extremo_uno_original[0] == limite_extremo_dos_original[0]:
        #     Originalmente el segundo extremo está abajo
        # Se mantiene el orden
        limite_extremo_uno = limite_extremo_uno_original
        limite_extremo_dos = limite_extremo_dos_original

    elif limite_extremo_uno_original[1] > limite_extremo_dos_original[1] \
            and limite_extremo_uno_original[0] == limite_extremo_dos_original[0]:
        # Originalmente el segundo extremo está arriba
        # Se invierten los límites
        limite_extremo_uno = limite_extremo_dos_original
        limite_extremo_dos = limite_extremo_uno_original

    # Reemplazo el límite correspondiente con el nuevo límite

    # Verifico si el nuevo límite está a la izquierda
    if nuevo_limite[0] < limite_extremo_uno[0] \
            and nuevo_limite[1] == limite_extremo_uno[1]:
        limite_extremo_uno = nuevo_limite

    # Verifico si el nuevo límite está a la derecha
    elif nuevo_limite[0] > limite_extremo_dos[0] \
            and nuevo_limite[1] == limite_extremo_dos[1]:
        limite_extremo_dos = nuevo_limite

    # Verifico si el nuevo límite está arriba
    elif nuevo_limite[1] < limite_extremo_uno[1] \
            and nuevo_limite[0] == limite_extremo_uno[0]:
        limite_extremo_uno = nuevo_limite

    # Verifico si el nuevo límite está abajo
    elif nuevo_limite[1] > limite_extremo_dos[1] \
            and nuevo_limite[0] == limite_extremo_dos[0]:
        limite_extremo_dos = nuevo_limite

    return limite_extremo_uno, limite_extremo_dos


def obtener_posicion_palabra(limite_extremo_uno, limite_extremo_dos):
    if limite_extremo_uno[0] != limite_extremo_dos[0]:
        # Si el valor de X cambia, la palabra se está generando de manera horizontal
        return 'H'
    else:
        return 'V'


def habilitar_derecha(window, casillero):
    # Habilito el casillero de la derecha
    window[(casillero[0] + 1, casillero[1])].update(disabled=False)
    window[(casillero[0] + 1, casillero[1])].update(button_color=('white', 'midnightblue'))


def habilitar_izquierda(window, casillero):
    # Habilito el casillero de la izquierda
    window[(casillero[0] - 1, casillero[1])].update(disabled=False)
    window[(casillero[0] - 1, casillero[1])].update(button_color=('white', 'midnightblue'))


def habilitar_arriba(window, casillero):
    # Habilito el casillero de arriba
    window[(casillero[0], casillero[1] - 1)].update(disabled=False)
    window[(casillero[0], casillero[1] - 1)].update(button_color=('white', 'midnightblue'))


def habilitar_abajo(window, casillero):
    # Habilito el casillero de abajo
    window[(casillero[0], casillero[1] + 1)].update(disabled=False)
    window[(casillero[0], casillero[1] + 1)].update(button_color=('white', 'midnightblue'))


def habilitar_tablero(window, limite_extremo_uno, limite_extremo_dos):
    if limite_extremo_uno is None:
        for x in range(MAX_COL):
            for y in range(MAX_ROWS):
                window[(x, y)].update(disabled=False)
                window[(x, y)].update(button_color=('white', 'midnightblue'))

    elif limite_extremo_uno is not None and limite_extremo_dos is None:
        if limite_extremo_uno[0] + 1 < MAX_COL:
            habilitar_derecha(window, limite_extremo_uno)

        if limite_extremo_uno[0] - 1 >= 0:
            habilitar_izquierda(window, limite_extremo_uno)

        if limite_extremo_uno[1] - 1 >= 0:
            habilitar_arriba(window, limite_extremo_uno)

        if limite_extremo_uno[1] + 1 < MAX_ROWS:
            habilitar_abajo(window, limite_extremo_uno)

    else:
        # Verifico si habilito horizontalmente o verticalmente
        posicion_palabra = obtener_posicion_palabra(limite_extremo_uno, limite_extremo_dos)

        if posicion_palabra == 'H':
            if limite_extremo_uno[0] - 1 >= 0:
                habilitar_izquierda(window, limite_extremo_uno)

            if limite_extremo_dos[0] + 1 < MAX_COL:
                habilitar_derecha(window, limite_extremo_dos)

        else:
            if limite_extremo_uno[1] - 1 >= 0:
                habilitar_arriba(window, limite_extremo_uno)

            if limite_extremo_dos[1] + 1 < MAX_ROWS:
                habilitar_abajo(window, limite_extremo_dos)


def habilitar_atril(window):
    for letra in range(CANTIDAD_LETRAS):
        if window[(letra, 'letra')].GetText() != '':
            window[(letra, 'letra')].update(disabled=False)


def deshabilitar_tablero(window):
    for x in range(MAX_COL):
        for y in range(MAX_ROWS):
            window[(x, y)].update(disabled=True)
            window[(x, y)].update(button_color=('white', 'black'))


def deshabilitar_atril(window):
    for letra in range(CANTIDAD_LETRAS):
        window[(letra, 'letra')].update(disabled=True)


MAX_ROWS = 10
MAX_COL = 10
CANTIDAD_LETRAS = 5

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z']

datos_tablero_a = [[randint(0, 1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

datos_tablero_b = []

for letra in range(0, CANTIDAD_LETRAS):
    datos_tablero_b.append(letras[randint(0, 26)])

tablero_a = [
    [sg.Button('', key=(x, y), font='Helvetica 12 bold', size=(4, 2), pad=(0.25, 0.25),
               button_color=('black', 'black'), disabled=True, enable_events=True)
     for x in range(MAX_COL)] for y in range(MAX_ROWS)
]

tablero_b = [[
    sg.Button(datos_tablero_b[x], key=(x, 'letra'), font='Helvetica 12 bold', size=(4, 2), pad=(10, 20),
              button_color=('black', 'darkgoldenrod'), border_width=1) for x in
    range(0, CANTIDAD_LETRAS)]]

sg.theme('Reddit')

layout = tablero_a + tablero_b + [[sg.Button('CANCELAR SELECCIÓN', key='cancelar',
                                             font='Helvetica 12 bold', size=(20, 2), pad=(4, 1),
                                             button_color=('white', 'darkred'), disabled=True)]]

window = sg.Window('Practica_04 | Ejercicio_10', layout, size=(800, 670), background_color='aliceblue',
                   element_justification='center')

casillero_seleccionado = None

# El límite uno será el que está más a la izquierda o más arriba
limite_extremo_uno = None

# El límite dos será el que está más a la derecha o más abajo
limite_extremo_dos = None

while True:
    event, values = window.read()

    print('event, values', event, values)

    if type(event) is tuple and event[1] == 'letra':
        casillero_seleccionado = event

        letra_seleccionada = window[event].GetText()

        habilitar_tablero(window, limite_extremo_uno, limite_extremo_dos)

        deshabilitar_atril(window)

        # window[casillero_seleccionado].update(visible=False)
        window[casillero_seleccionado].update('')

        window['cancelar'].update(disabled=False)

    if type(event) is tuple and event[1] != 'letra':
        window[event].update(letra_seleccionada)

        window['cancelar'].update(disabled=True)

        letra_seleccionada = None

        deshabilitar_tablero(window)

        habilitar_atril(window)

        if limite_extremo_uno is None:
            limite_extremo_uno = event

        elif limite_extremo_uno is not None and limite_extremo_dos is None:
            limite_extremo_dos = event
            nuevos_extremos = obtener_extremos(limite_extremo_uno, limite_extremo_dos, event)
            print('nuevos_extremos:', nuevos_extremos)
            limite_extremo_uno = nuevos_extremos[0]
            limite_extremo_dos = nuevos_extremos[1]

        elif limite_extremo_uno is not None and limite_extremo_dos is not None:
            nuevos_extremos = obtener_extremos(limite_extremo_uno, limite_extremo_dos, event)
            print('nuevos_extremos:', nuevos_extremos)
            limite_extremo_uno = nuevos_extremos[0]
            limite_extremo_dos = nuevos_extremos[1]

    if event == 'cancelar':
        window['cancelar'].update(disabled=True)

        # window[casillero_seleccionado].update(visible=True)
        window[casillero_seleccionado].update(letra_seleccionada)

        letra_seleccionada = None

        deshabilitar_tablero(window)

        habilitar_atril(window)

    if event in (None, 'Exit'):
        break

window.close()