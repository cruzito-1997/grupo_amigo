import os 
os.system("cls")


# Lista global para almacenar los contactos
contactos = []

# Función para agregar un contacto
def agregar_contacto():
    try:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        # Cada contacto es una lista [nombre, telefono, email]
        contacto = [nombre, telefono, email]
        contactos.append(contacto)
        print("Contacto agregado correctamente.\n")
    except:
        print(f"Error al agregar contacto:")

# Función para mostrar todos los contactos
def mostrar_contactos():
    try:
        if len(contactos) == 0:
            print("No hay contactos registrados.\n")
        else:
            print("Lista de contactos:")
            for i, contacto in enumerate(contactos, 1):
                print(f"{i}. Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Email: {contacto[2]}")
            print()
    except:
        print(f"Error al mostrar contactos:")

# Función para buscar un contacto por nombre
def buscar_contacto():
    try:
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        encontrado = False
        for contacto in contactos:
            if contacto[0].lower() == nombre_buscar.lower():
                print(f"Contacto encontrado: Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Email: {contacto[2]}\n")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.\n")
    except:
        print(f"Error al buscar contacto:")

# Función para eliminar un contacto por nombre
def eliminar_contacto():
    try:
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        eliminado = False
        for contacto in contactos:
            if contacto[0].lower() == nombre_eliminar.lower():
                contactos.remove(contacto)
                print("Contacto eliminado correctamente.\n")
                eliminado = True
                break
        if not eliminado:
            print("Contacto no encontrado, no se pudo eliminar.\n")
    except:
        print(f"Error al eliminar contacto:")

