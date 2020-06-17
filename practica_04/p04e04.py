""" En base al ejercicio 5 de la Práctica 3, diagramar una interfaz en PySimpleGUI que permita seleccionar dos archivos (utilizando el widget
FileBrowse). Uno de ellos contendrá colores y el otro coordenadas. Ambos archivos se encuentran en texto plano, donde cada elemento se ubica
en una línea. Utilizando el widget Graph, dibuje en cada coordenada, un
punto (con DrawPoint) del color asociado (correspondiente a la misma
línea de ambos archivos). Para realizar las pruebas, genere ambos archivos. Para generar el de colores, investigue los disponibles en el ejemplo
de colores en Github."""

import PySimpleGUI as sg

def obtener_datos(archivo):
    # print(archivo)
    with open(archivo, 'r') as archivo_colores:
        datos = archivo_colores.readlines()

    # print(datos)

    for pos, dato in enumerate(datos):
        datos[pos] = dato.splitlines()
        # print(datos[pos])

    # print(datos)

    return [elemento for lista_interna in datos for elemento in lista_interna]

def formatear_coordenadas(lista_coordenadas):
    lista_coordenadas_formateada = []
    temp = []
    for elem in lista_coordenadas:
        for coord in elem.split(", "):
            num = int(coord.replace("(", "").replace(")", ""))
            temp.append(num)
            if ")" in coord:
                lista_coordenadas_formateada.append(tuple(temp))
                temp = []

    return lista_coordenadas_formateada

def limpiar():
    window['archivo_colores'].update('')
    window['archivo_coordenadas'].update('')
    window['mostrar'].update(disabled=True)
    window['mostrar'].set_tooltip('Debe seleccionar ambos archivos.')
    graph.TKCanvas.delete('all')

sg.theme('Reddit')

layout = [
    [sg.Text('Seleccione el archivo que contiene los colores',
             font='arial 10 bold')],
    [sg.Text('* El mismo debe tener la extensión .txt y los colores deben estar separados por salto de línea',
             font='arial 8 italic')],
    [sg.In(key='archivo_colores', enable_events=True, disabled=True),
     sg.FileBrowse(target='archivo_colores',
                   file_types=(("Archivos de texto", "*.txt"), ("Archivos Python", "*.py"),))],
    [sg.Text('Seleccione el archivo que contiene las coordenadas',
             font='arial 10 bold')],
    [sg.Text('* El mismo debe tener la extensión .txt y las coordenadas deben estar separados por salto de línea',
             font='arial 8 italic')],
    [sg.In(key='archivo_coordenadas', enable_events=True, disabled=True),
     sg.FileBrowse(target='archivo_coordenadas',
                   file_types=(("Archivos de texto", "*.txt"), ("Archivos Python", "*.py"),))],
    [sg.Button('Limpiar', key='limpiar', button_color=('white', 'gray')),
     sg.Button('Mostrar coordenadas', key='mostrar', button_color=('white', 'green'), disabled=True,
               tooltip='Debe seleccionar ambos archivos.')],
    [sg.Graph(canvas_size=(475, 200), graph_bottom_left=(-100, -100), graph_top_right=(400, 400),
              background_color='lightgray',
              key='graph')],
    [sg.Exit('Salir', key='salir', button_color=('white', 'darkred'))]
]

window = sg.Window("Práctica_04 | Ejercicio_04", layout)
window.Finalize()

graph = window['graph']

while True:
    event, values = window.read()

    if event in (None, 'Exit', 'salir'):
        break

    if event in ('archivo_colores', 'archivo_coordenadas'):
        if len(values['archivo_colores']) > 0 and len(values['archivo_coordenadas']) > 0:
            colores = obtener_datos(values['archivo_colores'])
            coordenadas = obtener_datos(values['archivo_coordenadas'])

            coordenadas = formatear_coordenadas(coordenadas)

            window['mostrar'].update(disabled=False)
            window['mostrar'].set_tooltip('Haga clic para mostrar las coordenadas en la lista.')
        else:
            window['mostrar'].update(disabled=True)
            window['mostrar'].set_tooltip('Debe seleccionar ambos archivos.')

    if event == 'limpiar':
        limpiar()

    if event == 'mostrar':
        for index, elem in enumerate(colores):
            graph.DrawPoint(coordenadas[index], 8, color=elem)