lista = ['Auto', '123', 'Viaje', '50', '120']
listaX = []
for i in lista:
    if i.isdecimal():   #si i es decimal es True, devuelve un boolean
        x = int(i)  #convierto el string a integer
        listaX.extend([x])  #agrego x a la lista
listaX.sort()    #sort ordena la lista
print('vvv lista generada vvv\n', listaX)