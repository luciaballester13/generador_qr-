"""Generador de códigos QR.

Le pide al usuario un texto o una URL, el nombre del archivo y un color,
y genera una imagen PNG con el código QR.

El código está dividido en módulos propios:
    - generador.py: genera y guarda el QR.

Ejecución:
    python main.py
"""


from generador import generar_qr  
# Se importa la función del módulo propio


"Texto de bienvenida"
print(
    "Bienvenida/o al programa. Acá vas a poder generar tu código QR.\n"
    "Completá los datos que se piden a continuación.")


def solicitar_texto() -> str:
    """
    Solicita al usuario el texto o URL para generar el QR.

    Returns:
        str: Texto ingresado por el usuario.
    """
    
    texto = input("Ingrese un texto o URL: ").strip()

    if not texto:
        raise ValueError("El texto no puede estar vacío.")

    return texto


def solicitar_nombre_archivo() -> str:
    """
    Solicita el nombre del archivo de salida.

    Returns:
        str: Nombre del archivo.
    """
    nombre = input(
        "Ingrese el nombre del archivo o la ruta completa\n"
        "(ej: MiPrimerQR o C:\\Users\\Administrator\\QRs\\MiPrimerQR): "
    ).strip()

    if not nombre:
        raise ValueError("El nombre del archivo no puede estar vacío.")

    if not nombre.lower().endswith(".png"):
        nombre += ".png"

    return nombre


def solicitar_color() -> str:
    """
    Solicita al usuario seleccionar un color válido para el QR.

    Returns:
        str: Color seleccionado.
    """
    colores_disponibles = {
        "1": "Pink",
        "2": "Brown",
        "3": "Red",
        "4": "Green",
        "5": "Blue",
        "6": "Yellow",
        "7": "Black",
        "8": "White",
        "9": "Purple",
        "10": "Orange",
        "11": "Gray",
    }

    print("\nColores disponibles:")
    print("1. Rosa")
    print("2. Marrón")
    print("3. Rojo")
    print("4. Verde")
    print("5. Azul")
    print("6. Amarillo")
    print("7. Negro")
    print("8. Blanco")
    print("9. Violeta")
    print("10. Naranja")
    print("11. Gris")

    opcion = input(
        "\nSeleccione un color (1-11): ").strip()
    if opcion not in colores_disponibles:
         raise ValueError(
            "Debe seleccionar una opción válida entre 1 y 11."
        )
    if opcion == "8":
        raise ValueError(
            "El color blanco no es válido porque el QR no sería visible."
        )

    return colores_disponibles[opcion]


def main() -> None:
    """
    Función principal del programa.
    """
    try:
        texto = solicitar_texto()
        archivo = solicitar_nombre_archivo()
        color = solicitar_color()

        ruta = generar_qr(texto=texto, archivo=archivo, color=color)

        print("\n✅ QR generado correctamente")
        print(f"📁 Archivo guardado en:")
        print(ruta)
        print("Muchas gracias por utilizar nuestro programa,"
              "esperamos que le haya sido de mucha ayuda."
              "\n¡Hasta la próxima!")

    except ValueError as error:
        print(f"❌ Error de validación: {error}")

    except PermissionError:
        print("❌ No tiene permisos para guardar " "el archivo.")

    except OSError as error:
        print(f"❌ Error al guardar el archivo: "f"{error}")


if __name__ == "__main__":
    main()
    
   