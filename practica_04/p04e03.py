import json
from pattern.es import parse, conjugate
from pattern.es import INFINITIVE, PRESENT, PAST, SG, PL, SUBJUNCTIVE, PERFECTIVE, IMPERFECT, PRETERITE

"""Leer un texto desde un archivo y generar uno nuevo (denominado verbos.json) que contenga una estructura con todos los verbos convertidos
a infinitivo junto con la cantidad de apariciones de cada uno"""

with open("p04e03_Datos.txt", "r") as archivo:
    datos = archivo.read().split(', ')

verbos = []

for palabra in datos:
    #print(parse(palabra))
    #print(parse(conjugate(palabra, INFINITIVE)))
    if parse(conjugate(palabra, INFINITIVE)).split('/')[1] == 'VB':
        verbos.append(parse(conjugate(palabra, INFINITIVE)).split('/')[0])
    #print()

#print(verbos)
diccionario = {}
dt_string = 'verbos'
diccionario[dt_string] = verbos

#guardo el diccionario en un archivo json
with open('verbos.json', "w") as archivo_nuevo:
    json.dump(diccionario, archivo_nuevo)