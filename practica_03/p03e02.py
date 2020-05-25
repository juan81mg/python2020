frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'''
#separo la frase en cadenas por espacio
frase_separada = frase.split(' ')
#recorro la frase, cadena por cadena
res = {}
for cadena in frase_separada:   
    cant = len(cadena)
    res.setdefault(cant, [])
    #evaluo si estan repetidas
    test = res[cant]
    if not (cadena in test):   
        res[cant].append(cadena)
print('<<< resultado >>>\n', res)