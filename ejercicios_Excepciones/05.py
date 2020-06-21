"""
5. Analice el siguiente código e indique teniendo en cuenta que se ingresa el 0 como num2 en
algunos de los casos, si la excepción es capturada y por cuál de los bloques try/except del
código.¿La ejecución del código continua en este caso?
"""
#rta: la excepcion ZeroDivisionError es capturada por el bloque mas externo, 
# la ejecucion del codigo se interrumpe porque el while esta dentro del try

def divido(x, y):
    try:
        return x/y
    except KeyError:    #no se ejecuta nunca, no se esta usando diccionario en el codigo
        print("Ojo. Se produjo un error")

#leo una cantidad
cantidad = int(input("Ingrese un valor de 1 a 20: "))

try:
    while cantidad > 0:
        #leo dos números
        num1 = int(input('Ingrese un valor entero '))
        num2 = int(input('Ingrese otro valor entero '))
        result = divido(num1, num2)
        print("El resultado de la división entre", num1, "y", num2, "es: ",result)
        cantidad = cantidad - 1
except ZeroDivisionError:
    result = "Indefinido"

print("Se continúa con la ejecución")