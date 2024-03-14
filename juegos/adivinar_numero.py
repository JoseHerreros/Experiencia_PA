import random

def adivinar_numero(n):
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    texto = "Le achuntaste"
    numero = random.randint(1,10)
    if numero == n:
        print(texto)
        return
    print(f"Incorrecto, el numero era {numero}")
    return

print("Introduce un numero")
a = input()
adivinar_numero(a)
    