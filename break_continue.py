def run():
    ##uso de la palara clave continue
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print (contador)


    ##uso de la palara clave break
    # for i in range(10000):
    #     print(i)
    #     if i == 5137:
    #         break


    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()