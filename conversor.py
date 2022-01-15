from this import d
from tkinter import E

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
    print("********Pesos colombianos a dólares**********")
    pesos = input("¿Cuántos pesos colombianos tienes? \n")
    pesos = float(pesos)
    valor_dolar = 4007.24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("-----------------------------------------------------")
    print("Tus pesos convertidos a dólares son $" + dolares + " dólares")
elif opcion == '2':
    print("********Pesos mexicanos a dólares**********")
    pesos = input("¿cuantos pesos mexicanos tienes? \n")
    pesos = float(pesos)
    valor_dolar = 20.3049
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("-----------------------------------------------------")
    print("Tus pesos son equivalentes a $" + dolares + " dólares")
elif opcion == '3':
    print("********Soles peruanos a dólares**********")
    soles = input("¿Cuántos soles tienes? \n")
    soles = float(soles)
    valor_dolar = 3.87221
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("-----------------------------------------------------")
    print("Tus soles son equivalentes a $" + dolares + " dólares")
else:
    print('Ingresa una opción correta, por favor')