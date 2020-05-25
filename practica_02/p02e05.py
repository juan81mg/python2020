lis = []
op = 9
while op != 0:
    op = int(input('1: ingresar numeros\n2: ordenar numeros\n3: calcular el maximo\n4: calcular el minimo\n5: calcular el promedio\n0: para terminar\n'))
    if op == 1:
        n = int(input('Ingrese el numero para agregar: '))
        lis.append(n)
        print('numero ingresado con exito >>> ', lis)
    elif op == 2:
        lis.sort()
        print('la lista esta ordenada >>> ', lis)
    elif op == 3:
        print('el numero maximo de la lista es >>> ', max(lis))
    elif op == 4:
        print('el numero minimo de la lista es >>> ', min(lis)) 
    elif op == 5:
        prom = sum(lis)/len(lis)
        print('el promedio de los numeros de la lista es >>> ', prom)
if len(lis) == 0:
    print('>>> La lista esta vacia <<<')
else: print('<<< Operacion Terminada >>>')