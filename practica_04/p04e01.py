import PySimpleGUI as sg
from datetime import datetime
import json
"""
Diagrame una interfaz en PySimpleGUI que permita ingresar dos datos:
temperatura y humedad, junto con la fecha y hora actual. Al presionar
Añadir , deberá cargar los valores en una lista (Listbox). Añada un botón,
que permita guardar esta información en un archivo en formato json.
"""
# funcion que guarda la lista en un archivo
def save(lista):
    # creo un archivo en modo escritura
    archivo = open('p04e01_Datos_Temperatura_Humedad.dat', 'w')
    # guardo en formato json, serializo la lista y la guardo en el archivo
    json.dump(lista, archivo)
    # cierro el archivo
    archivo.close()
# funcion para ir agregando al listbox los datos de la lista y la fecha y hora
def update_list(listbox, lista):
    # actualizo el listbox con los datos, fecha y hora
    listbox.Update(map(lambda x: '{} : {} - {} - {}'.format(x[0], x[1], x[2], x[3]), lista))
# contenido de layout, que es una lista
layout = [
    [sg.Text('Temperatura'), sg.Input(key = 'temperatura')],
    [sg.Text('Humedad'), sg.Input(key = 'humedad')],
    [sg.Listbox(values = [], key = 'datos', size = (30,10))],
    [sg.Button('Añadir'), sg.Button('Guardar')]]
# titulo de la ventana y abre la ventana con el contenido layout
window = sg.Window("Temperatura y Humedad").Layout(layout)
# creo la lista para guardar los datos que se van añadir
lista = []
# bucle para añadir en una lista, listBox
while True:
    # ejecuta y crea la ventana, guarda los valores, primero el () sg.button y luego los valores que se ingresaron, los Input
    event,values = window.Read()
    # si cerramos la ventana el evento va ser None
    if event is None:
        break
    if event is "Añadir":
        # guardo la fecha y hora en distintas variables
        fecha = datetime.now().strftime('%d/%m/%Y')
        hora = datetime.now().strftime('%H:%M:%S')
        # si presiono añadir va agregando los valores a una lista
        lista.append((values['temperatura'], values['humedad'], fecha, hora))
        # mando el elemento 'datos', que es el listbox y la lista con los valores
        update_list(window.FindElement('datos'), lista)
    if event is "Guardar":
        # llamo a la funcion para guardar la lista en un archivo en formato json
        save(lista)
        break