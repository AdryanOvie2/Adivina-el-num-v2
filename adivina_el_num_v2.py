# En este juego la IA intentará adivinar el num
import random


def adivina_el_num2(num):
    print("==================================")
    print("       Bienvenid@ al juego!       ")
    print("==================================")
    print(f"Selecciona un número entre 1 y {num} para que la IA intente adivinarlo...")

    limite_inferior = 1
    limite_superior = num
    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
        
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta ingresa (A). Si es muy baja ingresa (B). Si es correcto ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    print(f"Correcto la IA ha adivinado el número {num} correctamente.")


adivina_el_num2(12)