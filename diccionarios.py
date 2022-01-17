def run():
    ##listas
    mi_lista = [1,2,3,4,5]
    # print(mi_lista)
    # print(mi_lista[2])
    mi_lista2 = [6,7,8,9]
    #une dos listas
    lista_final = mi_lista + mi_lista2
    ##agrega un elemento a la lista
    lista_final.append('Gabriela')
    # print(lista_final)
    ##recorre una lista
    # for item in lista_final:
    #     print(item)
    ##elimina un elemento de la lista
    lista_final.pop(9)
    # print(lista_final)

    ##tuplas
    # print('************************')
    mi_tupla = (1,2,3,4)
    mi_tupla2 = lista_final

    # print(mi_tupla2)

    # for value in mi_tupla2:
    #     print(value)

    #el diccionario contiene llaves y valores
    print('************************')
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina' : 44938712,
        'Brasil' : 210147125,
        'Colombia': 50372424
    }

    ##recorrer y pintar las keys de un diccionario
    # for pais in poblacion_paises.keys():
    #     print(pais)
    
    ##recorrer y pintar los values de un diccionario
    # for pais in poblacion_paises.values():
    #     print(pais)
    
    ##recorrer y pintar ambos, key y value
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene "+ str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()