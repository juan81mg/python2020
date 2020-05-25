tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista1 = []
lista2 = []
num=input('Ingrese un numero\n')
for i in tam:
    aux1 = i.partition(' ') #separo por ' ' cada dato de la lista
    aux4 = aux1[0]  #guardo la etiqueta
    aux2 = aux1[2]  #separo las cordenadas
    aux3 = aux2.split(',')  #separo las cordenadas en x e y
    x = int(aux3[0])
    y = int(aux3[1])
    if x >= int(num):  #evaluo x
        lista1.extend([aux4, (x, y)])
    else: 
        lista2.extend([aux4, (x, y)])
print('lista de coordenada X mayor o igual que el numero\n', lista1)
print('lista de coordenada X menor que el numero\n', lista2)