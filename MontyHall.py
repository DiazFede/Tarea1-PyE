import random

def monty_hall(cambiar):
    puertas = [1, 2, 3]
    auto = random.choice(puertas)
    eleccion = random.choice(puertas)

    # Monty revela una puerta con cabra
    posibles_para_abrir = [p for p in puertas if p != eleccion and p != auto]
    if len(posibles_para_abrir) == 1:
        monty_abre = posibles_para_abrir[0]
    else:
        monty_abre = random.choice(posibles_para_abrir)

    if cambiar:
        # El jugador cambia su elección
        nueva_eleccion = [p for p in puertas if p != eleccion and p != monty_abre][0]
        resultado = "Gana" if nueva_eleccion == auto else "Pierde"
    else:
        nueva_eleccion = eleccion
        resultado = "Gana" if eleccion == auto else "Pierde"

    print(f"Puerta elegida inicialmente: {eleccion}")
    print(f"Puerta con el auto: {auto}")
    print(f"Puerta abierta por el presentador: {monty_abre}")
    if cambiar:
        print(f"Nueva puerta elegida tras el cambio: {nueva_eleccion}")
    print(f"Resultado: {resultado}")
    return resultado == "Gana"

def simular(n, cambiar):
    exitos = 0
    for _ in range(n):
        if monty_hall(cambiar):
            exitos += 1
    probabilidad_empirica = exitos / n
    print(f"Jugadas: {n}, Cambia puerta: {cambiar}, Ganó: {exitos} veces")
    print(f"Probabilidad empírica de ganar: {probabilidad_empirica}")
    return probabilidad_empirica


simular(1000, cambiar=False)  
simular(1000, cambiar=True)   

simular(10000, cambiar=False)  
simular(10000, cambiar=True)  

simular(100000, cambiar=False)  
simular(100000, cambiar=True)  