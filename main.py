import os 
from function import * 

while True:
    print("1.	Agregar un contacto: nombre, teléfono, email.")
    print("2.	Listar contactos: mostrar todos los contactos guardados.")
    print("3.	Buscar un contacto por nombre.")
    print("4.	Eliminar un contacto.")
    print("5.	Salir del programa.")
    try:
        opcion = int(input("ingrese la opcion:\n"))
        if opcion == 1:
            print("agregar contactos")
        elif opcion == 2:
            print("Listar contactos: ")
        elif opcion == 3:
            print("	Buscar un contacto por nombre")
        elif opcion == 4:
            print("Eliminar un contacto")
        elif opcion == 5:
            print("salir de progama")
    except:
        print("ingrese caracteres")