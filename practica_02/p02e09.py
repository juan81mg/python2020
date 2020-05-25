# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

#cambio el 20 por 50 para extender el rango de numeros a adivinar
number = random.randint(1, 50)  #diferencia entre randint y randrange es que al usar randint(1, 10), el 10 es incluido dentro del rango
print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')

for guessesTaken in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number: #cuando encuentra el numero corta con break
        break

    if guessesTaken == 2:   #doy pista en el 3 intento
        if (number%2) == 0: 
            print('Tip: the guess number is pair')
        else: print('Tip: the guess number is odd')

if guess == number: #cuando adivina le numero arma el mensaje
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')