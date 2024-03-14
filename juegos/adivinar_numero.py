import random

def adivinar_numero():
    
    def chequear(n):
        texto = "Le achuntaste!"
        n = int(n)
        numero = random.randint(1,10)
        if numero == n:
            print(texto)
            return
        print(f"Incorrecto, el numero era {numero}")
        return

    print("Introduce un numero del 1 al 10")
    a = input()
    chequear(a)

    input("Aprete cualquier tecla para volver al menu")
    return
