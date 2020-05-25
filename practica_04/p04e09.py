import PySimpleGUI as sg 
import string
import random
"""
Generar un tablero A con casilleros de 10 x 10 y un tablero B con una
única fila que contenga 5 letras al azar. 
El objetivo del ejercicio es que se puedan situar una por una, 
las letras del tablero B al tablero A haciendo clic sobre cada una de las letras.
La mecánica sugerida es la de utilizar un clic para elegir 
una letra del B y otro clic sobre algún casillero del tablero A. 
Nota: no se debe permitir que se pueda agregar una letra sobre un
casillero ocupado. 
Se deberán agregar todas las letras disponibles.
"""
# seteo de colores
sg.theme('DarkBlue14')

#Comportamiento de los botones
# definicion clase BotonB para la fila de botones con letras
class buttonA():
    def __init__ (self,x,y):
        self.name = random.choice(string.ascii_letters)
        self.x = x
        self.y = y
        self.state = 1
        self.disabled = False
        self.key = (x,y)
        self.button = sg.Button(self.name, 
            auto_size_button = False,
            border_width = 2,
            disabled = self.disabled,
            focus = False,
            key = self.key,
            pad = (1,1))
    def update(self):
        self.button.update(disabled=self.disabled)
    def getLetra(self):
        return self.name
    def enable(self):
        self.disabled = False 
        self.update()
    def disable(self):
        self.disabled = True
        self.update()

#deficion de clase BotonA es para el grid de 10x10
class buttonB():
    def __init__ (self,x,y):
        self.name = " "
        self.x = x
        self.y = y
        self.state = 0   #si state es 0, no tiene valor, si es 1 ya tiene valor
        self.disabled = False
        self.key = (x,y)
        self.button = sg.Button(self.name, 
            auto_size_button = False,
            border_width = 2,
            disabled = self.disabled,
            focus = False,
            key = self.key,
            pad = (1,1))
    def update(self):
        self.button.update(self.name,disabled=self.disabled)
    def setLetra(self,name):
        self.name = name
        self.disabled = True   
        self.state = 1
        self.update()
    def disable(self):
        self.disabled = True
        self.update()
    def enable(self):
        self.disabled = False
        self.update()

# atril con las 5 letras random
b1 = [[0 for j in range(5)] for i in range(5)]

# grid de 10x10
b2 = [[0 for j in range(10)] for i in range(10)]

# definicion tablero B
def button1(x,y):
    #defino la lista con los atributos de buttonB
    b1[x][y] = buttonA(x,y)
    # devuelvo el boton
    return b1[x][y].button

# definicion tablero A
def button2(x, y):
    #defino la lista con los atributos de buttonB
    b2[x][y] = buttonB(x,y)
    # devuelvo el boton
    return b2[x][y].button

# estructura de la ventana
ventana = [
    [sg.Text("Tablero B")],
    [button1(z, 1) for z in range(5)],
    [sg.Text("Tablero A")] 
    ] + [
    [button2(x, y) for x in range(10)] for y in range(10)]

# creo el tablero
win = sg.Window("Practica_04 | Ejercicio_09", layout=ventana, finalize=True)

# funciones para controlar que no se rompa el programa haciendo click 2 veces en la misma tabla,
# funcion para deshabilita el valor de cada boton del grid de 10x10
def disable_A():
    for i in range(10):
        for j in range(10):
            b2[i][j].disable()

# funcion para habilitar los boton para guardar la letra
def enable_A():
    for i in range(10):
        for j in range(10):
            #pregunto el estado del boton para no volver a activar un boton con valor, evita la sobreescritura
            if (b2[i][j].state == 0):
                b2[i][j].enable()

#habilita la accion de cada boton del atril
def enable_B():
    for i in range(5):
        b1[i][1].enable()

#deshabilita el comportamiento de cada boton del atril
def disable_B():
    for i in range(5):
        b1[i][1].disable()

# booleano para que no se haga asigne un valor en un casillero lleno
ok = True

while True:
    # ejecuto la ventana y guardo los botones y los valores
    event, values = win.read()
    # si se cierra la ventana, corta
    if event is None:
        break
    # inicializo el tablero A de 10x10
    disable_A()
    # accion de la habilidad
    if (ok):
        x, y = event
        # guardo la letra del atril
        letra = b1[x][y].getLetra()
        #control
        ok = False
        # habilito para guardar la letra
        enable_A()
        # deshabilito en el atril el boton de la letra
        disable_B()
    else:
        x, y = event
        # le asigno la letra del atril en el grid
        b2[x][y].setLetra(letra)
        #control
        ok = True
        # habilito los botones del atril para empezar de nuevo
        enable_B()