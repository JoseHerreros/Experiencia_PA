import random
def memoria():
    lista = ['0','1','2','3','4','5','6','7','8','9']
    random.shuffle(lista)
    print(f"Memoriza la secuencia: {lista[0:5]}")
    respuesta = input("¿Cual era la secuencia? (escribe los numeros separandolos con comas ej: 1,2,3,4,5):")
    palabra = ','.join(lista[0:5])
    if respuesta == palabra:
        print("CORRECTO! Ganaste")
    else:
        print("INCORRECTO, Intenta nuevamente")
        
    input("Aprete cualquier tecla para volver al menu")
    return
