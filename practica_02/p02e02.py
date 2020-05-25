tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista = []
for i in tam:
    aux1 = i.partition(' ') #separo por ' ' cada dato de la lista
    aux2 = aux1[2]  #guardo las cordenadas
    aux3 = aux2.split(',')  #separo las cordenadas en x e y
    x = int(aux3[0])
    y = int(aux3[1])
    lista.extend([(x, y)])
lista.sort()    #sort ordena la lista
print('vvv lista ordenada vvv\n', lista)