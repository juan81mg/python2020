anim={'Gato Montes':2, 'Yacare overo':4, 'Boa acuatica':5}
pal = anim.keys()   #guardo todas las palabras en pal
lista = []
for i in anim:  #recorro todo el diccionario
    cadena = ''
    letra = anim[i] #guardo el valor de cada palabra
    cant = 0
    for y in i: #recorro caracter por caracter
        if (letra != cant): #mientras la posicion de la letra sea distinta del valor
            cadena = cadena + '_ '
        else: 
            cadena = cadena + y
        cant = cant + 1
    lista.append(cadena)
print('<<< Resultado >>>\n')
for x in lista:
    print(x, '\n')