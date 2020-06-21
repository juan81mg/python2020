"""
2. Indique si siempre se imprime el texto “la cantidad de divisiones realizadas fue: ”
"""
#rta: cuando no hay ninguna excepcion se ejecuta el else, pertenece al except

cantidad = 0
try:
    for x in range(4):
        num1 = int(input('Ingrese un dividendo '))
        num2 = int(input('Ingrese un divisor '))
        result = num1/num2
        cantidad = cantidad + 1
        print ("El resultado de la división entre",num1, "y", num2, "es: ",result)
        res = input("Desea continuar?: si/no ")
        if res == "si":
            num1 = int(input('Ingrese un dividendo '))  #se ejecuta pero no se evalua en ningun momento
            num2 = int(input('Ingrese un divisor '))    #se ejecuta pero no se evalua en ningun momento
        else:
            continua = False    #no se evalua en ningun momento
except ZeroDivisionError:
    print("El resultado de la division entre ", num1, " y ", num2 ,"indefinido")
else:
    print ("La cantidad de cuentas realizadas fue:", cantidad)