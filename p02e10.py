imagenes = ['im1', 'im2', 'im3']
coor = []
for i in range(3):
    ok = True
    while (ok): #repito hasta que la coordenada no este repetida
        print('\nIngrese las coordenadas para la imagen: ' + imagenes[i])
        x = int(input('ingrese la coordenada x >>> '))
        y = int(input('ingrese la coordenada y >>> '))
        xy = (x, y)
        #evaluo si esta repetida la coordenada
        if xy in coor:  
            print('\n>>> Coordenada repetida <<<')
            ok = True
        else:
            coor.append(xy)
            ok = False
#armo un diccionario para guardar el elemento de imagenes con su coordenada respectivamente
dic = dict()
for j in range(3):
    clave = imagenes[j]
    valor = coor[j]
    dic[clave] = valor
print('\nResultado del ingreso de coordenadas\n', dic)