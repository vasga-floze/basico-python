#funcion que valida si un numero es primo o no
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    ##verificar si un numero es primo
    numero = int(input('Escribe un numero: \n'))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()