
num1 = int(input('<<< Programa >>>\nIngrese el primer operando: '))
num2 = int(input('Ingrese el segundo operando: '))
op = int(input('Que operacion desea realizar:\n1: suma\n2: resta\n3: multiplicacion\n4: division\n'))
if op == 1:
    suma = num1 + num2
    print('la suma entre los numeros es >>> ', suma)
elif op == 2:
    resta = num1 - num2
    print('la resta entre los numeros es >>> ', resta)
elif op == 3:
    multi = num1 * num2
    print('la multiplicacion entre los numeros es >>> ', multi)
elif op == 4:
    div = num1 / num2
    print('la division entre los numero es >>> ', div) 
print('<<< finalizo el programa >>>')