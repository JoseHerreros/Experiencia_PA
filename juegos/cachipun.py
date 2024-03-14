import random

def cachipun():
    respuesta = input("¿piedra, papel o tijera?")
    lista = ["piedra", "papel", "tijera"]
    n = random.randint(0,2)
    compu = lista[n]
    print(f"Elegí: {compu}")
    if compu == respuesta:
        print("Empate")
    elif compu == "piedra" and respuesta == "tijera":
        print("Perdiste :(")
    elif compu == "papel" and respuesta == "piedra":
        print("Perdiste :(")
    elif compu == "tijera" and respuesta == "papel":
        print("Perdiste :(")
    else:
        print("Ganaste ;)")
    
    return
