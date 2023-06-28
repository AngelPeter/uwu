def obtener_colores_bandera(pais):
    colores_bandera = {
        "Argentina": ["celeste", "blanco"],
        "Brasil": ["verde", "amarillo"],
        "Canadá": ["rojo", "blanco"],
        "Francia": ["azul", "blanco", "rojo"],
        "India": ["naranja", "blanco", "verde"],
        "Colombia": ["amarillo", "azul", "rojo"],
      # Agrega más países y sus colores de bandera aquí
    }

    if pais in colores_bandera:
        colores = colores_bandera[pais]
        print(f"Los colores de la bandera de {pais} son: {', '.join(colores)}")
    else:
        print("No se encontró información sobre la bandera de ese país.")

# Ejemplo de uso
pais = input("Ingresa el nombre de un país: ")
obtener_colores_bandera(pais)

    #Yulian_Castaneda
    #Banderas
    #IEM_ESCUELA_NORMAL_PASTO
    #11-1
