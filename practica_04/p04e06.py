"""En base a los ejercicios anteriores, genere una ventana en la que se permita seleccionar un color de una lista (InputCombo, cargada desde el
archivo de colores) y los valores de x e y de las coordenadas (con dos Slider). Al presionar Añadir, deberá cargar los valores en una lista (Listbox).
Añada un botón, que permita guardar la lista de colores/coordenadas en
un archivo en formato json."""

import PySimpleGUI as sg
import json

def obtener_datos(archivo):
    with open(archivo, 'r') as archivo_colores:
        datos = archivo_colores.read()
    return datos

def actualizar_lista(componente_listbox):
    componente_listbox.Update(
        values=
        (
            # Si se quiere ordenar del clima agregado más antiguo a más reciente, invertir el orden de las listas
                [values['color'] + ' | ' + str(values['x']) + ' | ' + str(values['y'])] +
                window.Element('lista_colores_coordenadas').Values
        )
    )

def guardar_lista(nombre_archivo, datos_guardar):
    with open(nombre_archivo, 'w', encoding="utf-8") as archdatos:
        json.dump(datos_guardar, archdatos, ensure_ascii=False)
    sg.Popup('Archivo guardado correctamente.\n', title='¡Guardado con éxito!', button_color=('white', 'green'))

datos = obtener_datos('p04e05_Datos.txt')

# Convierto el string en un diccionario de diccionarios
datos = json.loads(datos)

# Obtengo todos los colores
colores = list(datos.keys())

sg.theme('Reddit')

colores_coordenadas_agregadas = []

layout = [
    [sg.InputCombo(key='color', values=[color for color in colores], size=(30, 1), enable_events=True)],
    [sg.Text('Eje X'),
     sg.Slider(key='x', range=(-100, 400), default_value=0, size=(20, 15), orientation='horizontal', disabled=True)],
    [sg.Text('Eje Y'),
     sg.Slider(key='y', range=(-100, 400), default_value=0, size=(20, 15), orientation='horizontal', disabled=True)],
    [sg.Button('Añadir', key='agregar', button_color=('white', 'green'), disabled=True,
               tooltip='Debe seleccionar un color.')],
    [sg.Text('Color | Eje X | Eje Y')],
    [sg.Listbox(values=[], size=(30, 10), key='lista_colores_coordenadas', enable_events=True)],
    [sg.Exit('Salir', key='salir', button_color=('white', 'darkred')),
     sg.Button('Guardar', key='guardar', button_color=('white', 'green'), disabled=True,
               tooltip='Debe agregar al menos elemento a la lista.')]
]

window = sg.Window("Práctica_04 | Ejercicio_06", layout)

while True:
    event, values = window.Read()

    if event in (None, 'Exit', 'salir'):
        break

    if event == 'color':
        window['x'].update(datos[values['color']]['x'])
        window['y'].update(datos[values['color']]['y'])
        window['agregar'].update(disabled=False)
        window['agregar'].set_tooltip('Agregar el elemento al listado.')

    if event == 'agregar':
        actualizar_lista(window['lista_colores_coordenadas'])
        window['guardar'].update(disabled=False)
        window['guardar'].set_tooltip('Guardar el listado.')
        colores_coordenadas_agregadas.append(
            {values['color']:
                {
                    "x": values['x'],
                    "y": values['y']
                }
            }
        )

    if event == 'guardar':
        guardar_lista('p04e06_Datos.json', colores_coordenadas_agregadas)