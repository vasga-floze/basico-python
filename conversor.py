from this import d
from tkinter import E

#definiendo una funcion
def conversor(tipo_pesos, valor_dolar):
    print("********" + tipo_pesos +" a dólares**********")
    pesos = input("¿Cuántos "+ tipo_pesos +" tienes? \n")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("-----------------------------------------------------")
    print("Tus " + tipo_pesos + " convertidos a dólares son $" + dolares + " dólares")

#El uso de las triple comillas doble permiten escribir cadenas de texto de varias lineas.
menu = """
¡Bienvenido al conversor de monedas! 💰

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Soles

Elige una opción: """

#se imprime el baner de bienvenida y se almacena la opcion ingresada por el usuario
opcion = input(menu)

#logica para procesar la opción ingresada por el usuario mediante condicionales
if opcion == '1':
    conversor('pesos colombianos', 4007.2)
elif opcion == '2':
    conversor('pesos mexicanos',20.3049)
elif opcion == '3':
    conversor('soles',3.87221)
else:
    print('Ingresa una opción correcta, por favor')