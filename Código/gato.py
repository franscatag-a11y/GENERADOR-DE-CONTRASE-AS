import secrets
import string


# ============================
# VARIABLES GLOBALES
# ============================

# Lista donde se almacenarán las contraseñas generadas
historial = []

# Tupla con los niveles de seguridad según la longitud
niveles_seguridad = (
    "Baja",
    "Media",
    "Alta"
)

# Diccionario que contiene los diferentes grupos de caracteres
# que pueden utilizarse para generar la contraseña
caracteres = {
    "minusculas": string.ascii_lowercase,
    "mayusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos": string.punctuation
}


# ============================
# FUNCIONES
# ============================

def evaluar_seguridad(longitud):
    """
    Determina el nivel de seguridad de una contraseña
    en función de su longitud.
    """

    if longitud < 8:
        return niveles_seguridad[0]

    elif longitud < 12:
        return niveles_seguridad[1]

    else:
        return niveles_seguridad[2]


def generar_contrasena(longitud,
                       usar_mayusculas,
                       usar_numeros,
                       usar_simbolos):
    """
    Genera una contraseña aleatoria utilizando los
    tipos de caracteres seleccionados por el usuario.
    """

    # Siempre se incluyen letras minúsculas
    conjunto = caracteres["minusculas"]

    # Agrega letras mayúsculas si el usuario lo solicita
    if usar_mayusculas:
        conjunto += caracteres["mayusculas"]

    # Agrega números si el usuario lo solicita
    if usar_numeros:
        conjunto += caracteres["numeros"]

    # Agrega símbolos si el usuario lo solicita
    if usar_simbolos:
        conjunto += caracteres["simbolos"]

    contrasena = ""

    # Genera la contraseña carácter por carácter
    # usando la librería secrets para mayor seguridad
    for _ in range(longitud):
        contrasena += secrets.choice(conjunto)

    return contrasena


def mostrar_historial():
    """
    Muestra todas las contraseñas generadas durante
    la ejecución del programa.
    """

    print("\n===== HISTORIAL =====")

    # Verifica si existen contraseñas almacenadas
    if len(historial) == 0:
        print("No existen contraseñas generadas.")

    else:
        # Recorre e imprime cada contraseña guardada
        for i, password in enumerate(historial, start=1):
            print(f"{i}. {password}")


# ============================
# PROGRAMA PRINCIPAL
# ============================

# Bucle principal del programa
while True:

    print("\n==============================")
    print(" GENERADOR SEGURO DE CONTRASEÑAS ")
    print("==============================")

    try:

        # Solicita la longitud de la contraseña
        longitud = int(
            input("Ingrese la longitud de la contraseña: ")
        )

        # Valida que la longitud mínima sea 8 caracteres
        while longitud < 8:
            print(
                "Error: La longitud mínima es 8 caracteres."
            )
            longitud = int(
                input("Ingrese nuevamente la longitud: ")
            )

        # Solicita las características deseadas
        mayusculas = input(
            "¿Incluir mayúsculas? (s/n): "
        ).lower() == "s"

        numeros = input(
            "¿Incluir números? (s/n): "
        ).lower() == "s"

        simbolos = input(
            "¿Incluir símbolos? (s/n): "
        ).lower() == "s"

        # Genera la contraseña con las opciones elegidas
        password = generar_contrasena(
            longitud,
            mayusculas,
            numeros,
            simbolos
        )

        # Guarda la contraseña en el historial
        historial.append(password)

        # Muestra la contraseña generada
        print("\nContraseña generada:")
        print(password)

        # Muestra el nivel de seguridad estimado
        print(
            f"Nivel de seguridad: "
            f"{evaluar_seguridad(longitud)}"
        )

        # Menú de opciones para el usuario
        opcion = input(
            "\n1. Generar otra contraseña\n"
            "2. Ver historial\n"
            "3. Salir\n"
            "Seleccione una opción: "
        )

        # Muestra el historial de contraseñas
        if opcion == "2":
            mostrar_historial()

        # Finaliza el programa
        elif opcion == "3":
            print("\nPrograma finalizado.")
            break

    # Captura errores cuando el usuario no ingresa números válidos
    except ValueError:
        print(
            "Error: Debe ingresar un número válido."
        )