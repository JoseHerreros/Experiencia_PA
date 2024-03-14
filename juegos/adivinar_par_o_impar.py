import random

def adivinar_par_o_impar():
    respuesta = input("Estoy pensando en un numero... Adivina ¿par o impar?:")

    def revisar(x):
        if x % 2 == 0:
            es = "par"
        else:
            es = "impar"
        return es
    
    n = random.randint(0,1000)
    correcto = revisar(n)
    if correcto == respuesta:
        print(f"CORRECTO, ganaste. El número era: {n}")
        return
    else:
        print(f"INCORRECTO, perdiste. El número era: {n}")
        return
