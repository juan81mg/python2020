"""
6. Analice el siguiente código e indique en qué caso se imprime el mensaje “La clave ingresada no
se encuentra en el diccionario”.
"""
# rta: la ezcepcion KeyError se ejecuta cuando la clave que se ingreso no existe en el diccionario

dicci = {1:"Juan", 2: "Ana", 5:"Helena"}
clave = input("Ingrese un valor (entre 1 y 5)")
try:
    print(dicci[clave])
except (KeyError):  #por ejemplo con 3
    print("La clave ingresada no se encuentra en el diccionario")