from functools import reduce

def operacion(oper, *args, **kargs):
    texto = ''
    if oper=='+':
        res = sum(args)
    if oper=='*':
        res = reduce((lambda x,y : x*y), args)
    for key, value in kargs.items():
        texto += key + "- " + value + " /"
    print('La operacion solicitada fue {}, el resultado es: {} por {}'.format(oper, res, texto))

operacion('*', 3, 4, 5, 8, 10, nombre='Juan', apellido='Gil', direccion='Calle 12')