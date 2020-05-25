frase='Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple.'
l=frase.split(' ') #genera una lista de palabras separadas por un espacio del string
#print(l)
newFrase=' '.join(l) #genera un string con una lista, juntando sus elementos con un espacio
print (newFrase)