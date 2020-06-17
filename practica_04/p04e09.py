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
#deficion de clase BotonA es para el grid de 10x10
class botonA():
    def __init__ (self,x,y):
        self.name = " "
        self.x = x
        self.y = y
        self.state = 0   #si state es 0, no tiene valor, si es 1 ya tiene valor
        self.disabled = False
        self.key = (x,y)
        self.button = sg.Button(self.name, 
            size = (4,2),
            button_color=('black', 'white'),
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

# definicion clase BotonB para la fila de botones con letras
class botonB():
    def __init__ (self,x,y):
        self.name = random.choice(string.ascii_letters)
        self.x = x
        self.y = y
        self.state = 1
        self.disabled = False
        self.key = (x,y)
        self.button = sg.Button(self.name, 
            size = (4,2),
            button_color=('white', 'black'),
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

# grid de 10x10
ba = [[0 for j in range(10)] for i in range(10)]

# atril con las 5 letras random
bb = [[0 for j in range(5)] for i in range(5)]

# definicion tablero A
def buttonA(x, y):
    #defino la lista con los atributos de buttonB
    ba[x][y] = botonA(x,y)
    # devuelvo el boton
    return ba[x][y].button

# definicion tablero B
def buttonB(x,y):
    #defino la lista con los atributos de buttonB
    bb[x][y] = botonB(x,y)
    # devuelvo el boton
    return bb[x][y].button

# funciones para controlar que no se rompa el programa haciendo click 2 veces en la misma tabla,


# funcion para habilitar los boton para guardar la letra
def enable_A():
    for i in range(10):
        for j in range(10):
            #pregunto el estado del boton para no volver a activar un boton con valor, evita la sobreescritura
            if (ba[i][j].state == 0):
                ba[i][j].enable()
# funcion para deshabilita el valor de cada boton del grid de 10x10
def disable_A():
    for i in range(10):
        for j in range(10):
            ba[i][j].disable()

#habilita la accion de cada boton del atril
def enable_B():
    for i in range(5):
        bb[i][1].enable()
#deshabilita el comportamiento de cada boton del atril
def disable_B():
    for i in range(5):
        bb[i][1].disable()


# estructura de la ventana
tableroA = [[sg.Text('Tablero A')]] + [[buttonA(x, y) for x in range(10)] for y in range(10)]
tableroB = [[sg.Text('Tablero B')]] + [[buttonB(z, 1) for z in range(5)]]
layout = tableroA + tableroB
win = sg.Window("Practica_04 | Ejercicio_09", layout, finalize=True)
ok=True
disable_A() # inicializo el tablero A de 10x10 para que no funcione el boton del grid al inicio
while True:
    event, values = win.read()

    if event is None:
        break

    disable_A() # inicializo el tablero A de 10x10
    if (type(event)==str)&(ok):      #control para que no se pise
        x = int(event[1])
        y = int(event[4])
        # print('x >>> ', x)
        # print('y >>> ', y)
        letra = bb[x][y].getLetra() # guardo la letra del atril
        # print('Letra >>> ', letra)
        enable_A()  # habilito para guardar la letra
        disable_B()     # deshabilito en el atril
        ok=False
    elif (ok==False):
        x = event[0]
        y = event[1]
        print(letra)
        # print('j >>> ', j, type(j))
        # print('i >>> ', i)
        # print('Letra >>> ', letra)
        ba[x][y].setLetra(letra)  # asigno la letra del atril en el grid
        enable_B()    # habilito los botones del atril para empezar de nuevo
        ok=True