#a
def suma(*args):
    res = 0
    cant = 0
    for n in args:
        if(cant != 30):
            res += n
            cant += 1
        else: break
    return res
#b
def imprimir(**kargs):
    for clave, valor in kargs.items():
        print('El {0} es {1}'.format(clave, valor))

datos = {'Nombre':'Juan', 'Apellido':'Gil', 'Sexo':'Varon'}
print(suma(1, 2, 3, 4))
imprimir(**datos)