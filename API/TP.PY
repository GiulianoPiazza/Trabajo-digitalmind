import random
import matplotlib.pyplot as plt
import numpy as np

# La clase Juego contiene métodos para:  jugar al piedra-papel-tijera (PPT), para adivinar un número, 
# tirar el dado y graficar una función.
class Juego:
    def jugar_ppt(self):
        opciones = ['piedra', 'papel', 'tijera']
        eleccion_computadora = random.choice(opciones)
        eleccion_usuario = input('Tenes que elegir: piedra, papel o tijera: ')
        if eleccion_usuario == eleccion_computadora:
            print('Es un empate!')
        elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
            print('Ganaste, te felicito!!!')
        else:
            print('Perdiste!')

    def adivinar_numero(self):
        numero = random.randint(1, 10)
        adivinanza = int(input('Adivina un número entre 1 y 10: '))
        if adivinanza == numero:
            print('Ganaste, te felicito!!!')
        else:
            print('Perdiste! El número era', numero)

    def tirar_dado(self):
        print('Sacaste un', random.randint(1, 6))

    def graficar_funcion(self):
        x = np.linspace(-10, 10, 100)
        funcion = input('Ingresa una función para graficar (por ejemplo, x/4, x**3, etc): ')
        y = eval(funcion)
        plt.plot(x, y)
        plt.show()

juego = Juego()


while True:
    opcion = input('Elige una opción: \n - (1) PPT \n - (2) Adivinar  \n - (3) Dado  \n - (4) Graficar \n - (5) Salir \n')
    if opcion == '1':
        juego.jugar_ppt()
    elif opcion == '2':
        juego.adivinar_numero()
    elif opcion == '3':
        juego.tirar_dado()
    elif opcion == '4':
        juego.graficar_funcion()
    elif opcion == '5':
        break