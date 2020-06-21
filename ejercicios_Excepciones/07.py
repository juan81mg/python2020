"""
7. Analice el siguiente código e indique en qué casos se va a producir la excepción KeyError y
por cuáles de los bloques try/except será capturada
"""
# rta: cuando se arma la lista si un valor es igual a 5 fuerza la excepcion, 
# la captura el bloque mas externo, porque el try interno no llega a ejecutarse.

import random

def genero_claves():
    claves = []
    for i in range(10):
        valor = random.randrange(10)
        if valor == 5:
            raise KeyError
        claves.append(valor)
    return claves

try:
    claves = genero_claves()
    for i in range(10):
        try:
            print(claves[i])
        except (KeyError):  #no se ejecuta nunca, no va haber una excepcion en la impresion de la lista
            print(claves)
            print("Se produjo un error al imprimir una clave")
except (KeyError):
    print("Se produjo un error general")