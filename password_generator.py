##simular el generador de contraseñas de firefox
import random


def generate_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'X', 'Y', 'Z']

    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'x', 'y', 'z']

    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{',
    '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^',
    '&', '$', '#', '"']

    ##combinar las listas en una sola lista
    characters = mayus + minus + chars + nums

    password = []

    for i in range(15):
        characters_random = random.choice(characters)
        password.append(characters_random)
    
    password = "".join(password) #aqui se convierte la lista a un string
    return password


def run():
    password = generate_password()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()