import random

def a():
    res = int(input('\nFuncion A:\nAdivine el Resultado >>> '))
    x = random.randrange(100)
    y = random.randrange(100)
    resultado = x + y
    if res == resultado:
        print('<<< Acerto >>>')
    else: print('>>> No Acerto <<< era', resultado)

def b():
    tipo = []
    palabras = [('grave', ['molesto']), ('aguda', ['ratón']), ('esdrujula', ['murciélago'])]
    for t in palabras:
        tipo.append(t[1])
    cant = len(tipo)    #guardo la cantidad de elementos de la lista tipo
    c = random.randrange(cant)  #elijo aleatoriamente un numero de la cantidad
    pal = tipo[c]   #elijo la palabra de la posicion c
    print ('\nFuncion B:\nQue tipo de palabra es >>>', pal)
    res = input(' grave, aguda o esdrujula??\n')
    resultado = palabras[c]
    if res == resultado[0]:
        print('<<< Acerto >>>')
    else: print('>>> No Acerto <<< era',resultado[0])

#Diccionario Ordenado sin repeticiones del ejercicio 5
colores = ['azul', 'amarillo', 'rojo', 'blanco', 'negro']
coordenadas = [(2,3), (5,6), (8,8), (10,2), (-5,-8)]
dic = {}
for x in coordenadas:
    dic[x] = random.choice(colores)
    colores.remove(dic[x]) #saco el color que ya use para que no se repita

#Ejercicio 6
funciones = [a, b]
for y in dic:
    color = dic[y]
    op = random.choice(funciones)
    if op == a:
        a()
    else: b()

print('\n ### FIN ###')