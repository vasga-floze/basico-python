#*******funciones*******

# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

#*****funciones con parametros*****
# def conversacion(mensaje):
#     print('Hola')
#     print('¿Cómo estás?')
#     print(mensaje)
#     print('Bye')


# opcion = int(input('Elige una opción (1, 2, 3):'))
# if opcion == 1:
#     #llamado a la funcion, pasando el parametro
#     conversacion('Elegiste la opcion 1')
# elif opcion == 2:
#     #llamado a la funcion, pasando el parametro
#     conversacion('Elegiste la opcion 2')
# elif opcion == 3:
#     #llamado a la funcion, pasando el parametro
#     conversacion('Elegiste la opcion 3')
# else:
#     print('Escribe una opción válida.')


#******funcion que recibe parametros y retorna un valor
def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)