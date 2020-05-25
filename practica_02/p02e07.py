cadena = input('<<< Programa >>>\nIngrese el string para saber si es palindromo: ')
cad = cadena.lower()
if cad == cad[::-1]:
    print('Es palindromo')
else:
    print('No es palindromo')
print('<<< finalizo el programa >>>')