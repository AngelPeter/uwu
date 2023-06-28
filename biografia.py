def crear_biografia(nombre, fecha_nacimiento, lugar_nacimiento, descripcion):
    biografia = f"Biografía de {nombre}\n\n"
    biografia += f"Fecha de nacimiento: {fecha_nacimiento}\n"
    biografia += f"Lugar de nacimiento: {lugar_nacimiento}\n\n"
    biografia += f"Descripción: {descripcion}\n"
    return biografia

# Solicitar información al usuario
nombre = input("Ingrese el nombre: ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
lugar_nacimiento = input("Ingrese el lugar de nacimiento: ")
descripcion = input("Ingrese una breve descripción: ")

# Crear la biografía
biografia = crear_biografia(nombre, fecha_nacimiento, lugar_nacimiento, descripcion)

# Imprimir la biografía
print("\n--- Biografía ---")
print(biografia)

    #Santiago_Enriquez
    #Biografia
    #IEM_ESCUELA_NORMAL_PASTO
    #11-1
