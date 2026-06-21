"""
Generador de contraseñas
-------------------------------------------
Este es un generador de contraseña que permite incluir (letras, números, símbolos)
y una longitud, genera una contraseña aleatoria, y pregunta si se
desea generar otra.
"""

import random
import string

seguir = "s"

while seguir == "s":
    # Pedir la longitud de la contraseña
    longitud = int(input("¿Cuántos caracteres quieres que tenga la contraseña? "))

    # Preguntar qué tipos de caracteres incluir
    incluir_letras = input("¿Incluir letras? (s/n): ").lower() == "s"
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    # Construir el conjunto de caracteres según lo elegido
    caracteres = ""
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += "!@#$%^&*"

    # Generar la contraseña eligiendo caracteres al azar
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    # Mostrar el resultado
    print("Tu contraseña es:", contrasena)

    # Preguntar si se desea generar otra contraseña
    seguir = input("\n¿Quieres generar otra contraseña? (s/n): ").lower()
    print()

print("¡Hasta luego!")