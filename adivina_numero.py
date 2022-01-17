##modulos son codigos reutilizables
##importar modulo 
import random

def run():
    #usando la funcion del modulo
    numero_aleatorio = random.randint(1, 100)
    #solicitando un numero al usuario
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    #comparando numero ingresado por el usuario con numero generado por la funcion
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(int(input('Elige otro número: ')))
    print('Ganaste!')


if __name__ == '__main__':
    run()