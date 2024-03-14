import random
def juego_del_dado():
    n_usuario = 0
    n_compu = 0

    print("Bienvenido al juego del dado, el primero en sumar 30 puntos gana.")

    def lanzar_dado():
        dado = random.randint(1,6)
        return dado
    
    def jugar(n):
        input("Presiona ENTER para lanzar el dado")
        dado = lanzar_dado()
        print(f"Obtuviste un {dado}")
        n = n + dado
        return n
    
    def jugar_compu(n):
        print("Ahora es mi turno de lanzar el dado")
        dado = lanzar_dado()
        print(f"Obtuve un {dado}")
        n = n + dado
        return n
    
    while n_usuario < 30 and n_compu < 30:
        n_usuario = jugar(n_usuario)
        n_compu = jugar_compu(n_compu)
        print(f"PUNTAJES PARCIALES: TU -> {n_usuario}, YO -> {n_compu}")

    
    gana_usuario = "ME HAS GANADO! Superaste los 30 puntos, felicidades."
    gana_compu = "PERDISTE! Llegué a los 30 puntos, intenta nuevamente."
    if n_usuario >= 30:
        print(gana_usuario)
    else:
        print(gana_compu)
        
    input("Aprete cualquier tecla para volver al menu")
    return

    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    
