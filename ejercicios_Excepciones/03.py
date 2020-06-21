"""
3. Analice este código y diga si el mensaje “La cantidad de cuentas realizadas fue:”, se imprime
SÓLO si todos los números “divisores” ingresados fueron distintos a cero.
"""
#rta: el else se imprime siempre haya una cuenta viable

cantidad = 0    #si lo comentamos se ejecuta la excepcion
try:
    for x in range(4):
        num1 = int(input('Ingrese un dividendo '))
        num2 = int(input('Ingrese un divisor '))
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Indefinido"
        cantidad = cantidad + 1
        print("El resultado de la división entre", num1, "y", num2, "es: ",result)
except NameError:   #estan todas las variables definidas, no se ejecuta nunca
    print("Alguna variable del código se está usando y no fue declarada")
else:
    print("La cantidad de cuentas realizadas fue:", cantidad)