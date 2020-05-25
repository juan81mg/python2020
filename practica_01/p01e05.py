frase='Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple'
frasem=frase.lower() #pasa todo el string a minuscula
l=frasem.split(' ') #genera una lista de un string separando sus elementos con un espacio
newFrase=set(l) #saca los repetidos y genera una list desordenada
print (newFrase)