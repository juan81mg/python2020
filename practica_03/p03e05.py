import random
colores = ['azul', 'amarillo', 'rojo', 'blanco', 'negro']
coordenadas = [(2,3), (5,6), (8,8), (10,2), (-5,-8)]
dic = {}
dic2 = {}
for x in coordenadas:
    dic[x] = random.choice(colores) #elemento al azar
for y in coordenadas:
    dic2[y] = random.choice(colores)
    colores.remove(dic2[y]) #saco el color que ya use para que no se repita
print('<<< Diccionario con repeticiones >>>\n', dic)
print('\n<<< Diccionario sin repeticiones >>>\n', dic2)