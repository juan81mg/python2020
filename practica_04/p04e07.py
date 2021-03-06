"""
Dado el archivo que detalla la cantidad de mujeres que estudian
carreras tecnológicas (Ver archivo mujeresEnCarrera.csv), realizar los siguientes ejercicios:
- Informar la cantidad total de estudiantes mujeres por universidad.
- Generar una interfaz en PySimpleGUI que muestre las cantidades
agrupadas por universidad ordenadas de mayor a menor.
- Mostrar las cantidades de cada universidad representadas por algún
elemento gráfico de tamaño proporcional a la cantidad mayor.
- Incorporar la posibilidad de seleccionar el archivo desde la misma
interfaz.
- Agregar la funcionalidad que el botón que permita ordenar esté deshabilitado hasta que se seleccione el archivo.
Nota: Investigue en el repositorio github del proyecto PySimpleGUI posibles ejemplos para utilizar gráficos
"""
import csv
import PySimpleGUI as sg
import random

# Functions
# calcula la proporcion
def cal_proporcion(valores):
    # devuelve tupla con el maximo: 0 universidad, 1 valor
    maximo = max(valores, key=lambda x: x[1]) [1]
    # limitamos a 75 pixeles como el tamano mas grande.
    tam_max = 75 
    return tam_max / int(maximo)

# constantes para el grafico
graf_ancho = 400
graf_alto = 170
# grafica la proporcion de los valores de la cantidad de mujeres
def graficar(grafico, valores):
    # calcula la proporcion 
    proporcion = cal_proporcion(valores)
    for valor in valores:
        # depende la proporcion va ser el diametro
        tam = proporcion * valor[1]
        # hace un random dentro del alto y ancho predefinido
        posicion = (random.randrange(graf_ancho), random.randrange(graf_alto))
        # genero un circulo por cada valor
        grafico.DrawCircle(posicion, tam, fill_color='black', line_color='white')

#ordena una lista de mayor a menor
def ordenar(list_cant_muj):
    return(sorted(list_cant_muj, key=lambda y: y[1], reverse=True))

# actuliza el listbox
def update_listbox(listbox, list_cant_muj):
    listbox.Update(map(lambda x: '{} : {}'.format(x[0], x[1]), list_cant_muj))

# columna de las estudiantes mujeres 
col_cant = 10
# columna de las universidades
col_uni = 2
# abre un archivo csv y devuelve una lista de cantidad de muejeres por universidad
def leer(origen):
    #creo un diccionario para la cantidad 
    cant = {}
    #abro el archivo .cvs
    archivo = open(origen, 'r', encoding='utf8')
    #hago legible el archivo
    csvreader = csv.reader(archivo, delimiter=',', quotechar='"')
    # salto la fila de los titulos de las columnas
    next(csvreader)
    # recorro el archivo fila por fila
    for row in csvreader:
        # guardo el nombre de la universidad
        uni = row[col_uni]
        # guardo en valor la cantidad de mujeres por uni que no este vacia o sea cero
        valor = (int(row[col_cant]) if row[col_cant] is not '' else 0)
        # busco en el diccionario si ya no lo agregue, y lo agrego o actualizo si corresponde
        if uni not in cant:
            cant[uni] = valor
        else: 
            cant[uni] += valor
    return cant

#PP
#layout
ancho = 400
alto = 170
menu = [
    [sg.Text('Archivo')],
    [sg.Input(), sg.FileBrowse(), sg.OK(), sg.Button('Cancelar')],
    [sg.Listbox(values=[], key='Universidad', size=(60,10)), 
    sg.Graph(canvas_size=(ancho, alto), graph_bottom_left=(0,0), 
    graph_top_right=(ancho, alto), background_color='red', key='grafico')],
    [sg.ReadButton('Ordenar', key='boton_ordenar', disabled=True)]
    ]
win = sg.Window('Practica_04 | Ejercicio_07', layout=menu, finalize=True)

# ejecucion
while True:
    event, values = win.read()
    #guardo en origen el path del archivo a leer
    origen = values[0]
    #cierro ventana o apreto en cancelar
    if event is None or event == 'Cancelar':
        break
    if event is 'OK':
        #habilito el boton ordenar
        win.FindElement('boton_ordenar').Update(disabled=False)
        # ok si hay un path cargado
        archivoOK = True
        dic_cant_muj = leer(origen)
        #convierto el diccionario usado en leer en una lista para actualizar el listbox
        list_cant_muj = dic_cant_muj.items()
        # grafico proporcional de la lista
        graficar(win.FindElement('grafico'), list_cant_muj)
        # actualizo el listbox
        update_listbox(win.FindElement('Universidad'), list_cant_muj)
    if event is 'boton_ordenar' and archivoOK:
        list_cant_muj_ord = ordenar(list_cant_muj)
        update_listbox(win.FindElement('Universidad'), list_cant_muj_ord)