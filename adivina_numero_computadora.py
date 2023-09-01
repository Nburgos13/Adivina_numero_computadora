import random

# Adivina el numero por la computadora


def adivina_el_numero_computadora (x):

    print("=" * 50)
    print("Bienvenido(a) al juego!")
    print("=" * 50)
    print(f"Seleciona un numero entre el 1 y {x} para que la computadora intente adivinarlo...")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""

    while respuesta != "c":

        # Generar una prediccion

        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        # Obtener una respuesta del usuario

        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). "
                          f"Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
            # Intervalo inicial: [1, 10]
            # Prediccion: 6
            # Respuesta: "a"
            # Intervalo: [1, 5]
        elif respuesta == "b":
            limite_inferior = prediccion + 1
            # Intervalo inicial: [1, 10]
            # Prediccion: 6
            # Respuesta: "b"
            # Intervalo: [7, 10]

    print(f"¡ Siiiii ! La computadora adivinó tu número correctamente: {prediccion}")


adivina_el_numero_computadora(10)