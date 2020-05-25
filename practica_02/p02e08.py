cadena = input('<<< Programa >>>\nIngrese el string para evaluar: ')
cad = cadena.lower()

#recorro la cadena y agregando al diccionario cada letra:cant
dic={}
for letra in cad:
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1

#recorro el dicionario evaluando si cada valor es primo
lis = []
for d in dic.items():
    valor = d[1]
    clave = d[0]
    cont = 0
    for i in range(1, valor+1):
        if (valor % i) == 0:
            cont = cont + 1
    if cont == 2:
        lis.append(clave)
    print('Cantidad de veces que aparece la letra ', clave,' >>> ', valor)

print('letras que aparecen primo veces >>> ', lis)

print('<<< finalizo el programa >>>')