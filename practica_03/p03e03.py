def agregar_jug(jugadores):
    ok = True
    while ok:
        nombre=input('Ingrese el nombre:\n')
        nivel=int(input('Ingrese el nivel alcanzado:\n'))
        puntaje=int(input('Ingrese el puntaje maximo:\n'))
        tiempo=int(input('Ingrese el tiempo de juego:\n'))
        jugadores[nombre]=[nivel, puntaje, tiempo]
        if (input('\ndesea agregar un nuevo jugador? (y/n)\n')) != 'y':
            ok = False
    return(jugadores)

def buscar_jug(jugadores):
    buscar = input('Ingrese el nombre del Jugador que desea buscar: ')
    if buscar in jugadores.keys():
        print('Los datos del jugador ', buscar, ' son ', jugadores[buscar])
    else: print(' >>> El jugador no existe <<<')

def mayor_puntaje(jugadores):
    max = 1
    for x in jugadores:
        i = jugadores[x][1]
        if (i > max):
            n = x
            max = i
    print ('El jugador con mayor puntaje es >>> ',n)

def agregar_jugada(jugadores):
    print('vvv Ingrese los datos de la Jugada vvv')
    nombre=input('Ingrese el nombre del jugador:\n')
    if nombre in jugadores.keys():
        nivel=int(input('Ingrese el nivel alcanzado:\n'))
        puntaje=int(input('Ingrese el puntaje maximo:\n'))
        tiempo=int(input('Ingrese el tiempo de juego:\n'))
        if puntaje > jugadores[nombre][1]:
            jugadores[nombre] = [nivel, puntaje, tiempo]
    else:
        print('El Jugador no Existe, elija la opcion 1')

def ranking(jugadores):
#    import operator
    dic = dict(sorted(jugadores.items(), key=lambda x:x[1], reverse=True))  #con operacion LAMBDA
#    dic = dict(sorted(jugadores.items(), key=operator.itemgetter(1), reverse=True))    #sin LAMBDA
    print('vvv Ranking 10 Mejores Puntajes vvv\n')
    i = 1
    for k,v in dic.items():
        if (i != 11):
            print('puesto ', i, ' >>> ', k, v)
            i = i + 1
        else: break

jugadores = {}
op = 9
while op != 0:
    op = int(input('1: Agregar un Jugador\n2: Buscar un Jugador\n3: Lista de Jugadores\n4: Jugador con Mayor Puntaje\n5: Agregar Jugada\n6: Ranking 10 Mejores Puntajes\n0: para terminar\n'))
    if op == 1:
        agregar_jug(jugadores)
        print('<<< opcion 1 con exito!!! >>>\n')
    elif op == 2:
        buscar_jug(jugadores)
        print('<<< opcion 2 con exito!!! >>>\n')
    elif op == 3:
        print('Lista de Jugadores\n', jugadores.keys())
        print('<<< opcion 3 con exito!!! >>>\n')
    elif op == 4:
        mayor_puntaje(jugadores)
        print('<<< opcion 4 con exito!!! >>>\n')
    elif op == 5:
        agregar_jugada(jugadores)
        print('<<< opcion 5 con exito!!! >>>\n')
    elif op == 6:
        ranking(jugadores)
        print('<<< opcion 6 con exito!!! >>>\n')

print('<<< FIN >>>\n',)