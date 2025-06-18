import os 
from function import * 






def menu():
    while True:
        print("=== Mini Agenda de Contactos ===")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: \n"))
            
            if opcion == 1:
                agregar_contacto()
            elif opcion == 2:
                mostrar_contactos()
            elif opcion == 3:
                buscar_contacto()
            elif opcion == 4:
                eliminar_contacto()
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente nuevamente.\n")
        except:
            print("Debe ingresar un número válido.\n")

menu()