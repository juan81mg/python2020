"""
1. Indique si ingresando los siguientes par de números el código se ejecuta siempre, si no es así
cómo modificaría el código para que se ejecute en todos los casos.
100, 2
10, 0
15, 3
"""
# rta: se produce una excepcion cuando se divide por 0 (10, 0), ZeroDivisionError, y deja ejecutar el try,
# poniendo el bloque del try dentro del while se podria ejecutar el codigo hasta que no se desee continuar.
# se puede solucionar con el siguiente codigo

# num1 = int(input('Ingrese un dividendo '))
# num2 = int(input('Ingrese un divisor '))
# cantidad = 0
# continua = True
# while continua:
#     try:
#         result = num1/num2
#         cantidad = cantidad + 1
#         print ("El resultado de la división entre",num1, "y", num2, "es: ",result)
#         res = input("Desea continuar?: si/no ")
#         if res == "si":
#             num1 = int(input('Ingrese un dividendo '))
#             num2 = int(input('Ingrese un divisor '))
#         else:
#             continua = False
#     except ZeroDivisionError:
#         result = "indefinido"
#         print('El resultado es ',result,' intente nuevamente...')
#         num1 = int(input('Ingrese un dividendo '))
#         num2 = int(input('Ingrese un divisor '))
# print ("La cantidad de cuentas realizadas fue:", cantidad)

num1 = int(input('Ingrese un dividendo '))
num2 = int(input('Ingrese un divisor '))
cantidad = 0
continua = True
try:
    while continua:
        result = num1/num2
        cantidad = cantidad + 1
        print ("El resultado de la división entre",num1, "y", num2, "es: ",result)
        res = input("Desea continuar?: si/no ")
        if res == "si":
            num1 = int(input('Ingrese un dividendo '))
            num2 = int(input('Ingrese un divisor '))
        else:
            continua = False
except ZeroDivisionError:
    result = "indefinido"
print ("La cantidad de cuentas realizadas fue:", cantidad)

