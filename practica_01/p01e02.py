#cant=0
frase='Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple.'
palabra=input('Ingrese una palabra:') #guarda lo que lee por teclado
l=frase.split(' ') #genera una list con los elementos del string que estan separados por blanco
#for i in l:#recorre la lista
#    if i == palabra: #compara el texto ingresado por teclado con cada elemento de la list
#        cant=cant+1 #cuenta la cantidad de coincidencias
print (l)
#print ('cantidad de veces que aparece la palabra en la frase', cant)
print('cantidad de veces que aparece la palabra: ', l.count(palabra)) 