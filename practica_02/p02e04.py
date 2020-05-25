from random import shuffle
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]
puntaje = 0 #inicializo el puntaje
shuffle(preguntas)  #desordeno la lista
print('+++++ Juego de Preguntas +++++\n')
for p in preguntas:
    print('>>> pregunta <<<\n', p[0])
    res = input('respuesta (si/no):')
    if (res == p[1]):  #evaluo la respuesta
        print('--->>> respuesta correcta\n')
        puntaje = puntaje + 1
    else:
        print('--->>> respuesta incorrecta\n')
print('su puntaje es >>>>>', puntaje)