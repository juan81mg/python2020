"""
4. Analice este código y diga si el mensaje “La cantidad de cuentas realizadas fue: ..”, se imprime
siempre dado que si se produce un error en la función “divido” lo atiende el bloque try except
más interno.
"""
# rta: se imprime siempre y cuando no haya una excepcion de NameError, como es este caso.

cantidad = 0

def divido(n1, n2):
    return n1/n2 #error de en la variable local n, no esta declarada, se tiene poner n1 en n

try:
    for x in range(4):
        num1 = int(input('Ingrese un dividendo '))
        num2 = int(input('Ingrese un divisor '))
        try:
            result = divido(num1, num2)
        except ZeroDivisionError:
            result = "Indefinido"
        cantidad = cantidad + 1
        print("El resultado de la división entre", num1, "y", num2, "es: ",
        result)
except NameError:
    print("Alguna variable del código se está usando y no fue declarada")
else:
    print("La cantidad de cuentas realizadas fue:", cantidad)