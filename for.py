def run():
    #imprime numeros hasta 1000 con el ciclo for
    # for contador in range(1, 1001):
    #     print(contador)

    
    #convertir rangos a listas
    # a = list(range(1001))
    # print(a)


    #imprime la tabla del 11 con el ciclo for
    # for i in range(10):
    #     print(11*i)


    #Recorriendo un string con for
    # nombre = input('Escribe tu nombre: ')
    # for letra in nombre:
    #     print(letra)

    
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run()