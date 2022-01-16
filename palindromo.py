#declara el metodo que procesara la cadena de textos
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1] 
    if palabra == palabra_invertida:
        return True
    else:
        return False

#define funcion principal
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es un palíndromo')


#ejecuta funcion principal
if __name__ == '__main__':
    run()