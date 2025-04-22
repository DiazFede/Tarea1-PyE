import random

def cumpleaños_simulacion(num_personas, num_simulaciones=10000):
    coincidencias = 0

    # Repetir el experimento num_simulaciones veces
    for _ in range(num_simulaciones):
        cumpleaños = []  # Lista para almacenar los cumpleaños de las personas

        # Asignar cumpleaños aleatorios a cada persona
        for _ in range(num_personas):
            cumple = random.randint(1, 365)  # Generar un cumpleaños aleatorio entre 1 y 365
            if cumple in cumpleaños:
                coincidencias += 1  # Si ya hay un cumpleaños igual, contar como coincidencia
                break
            cumpleaños.append(cumple)

    # Calcular la probabilidad empírica de coincidencia
    probabilidad = coincidencias / num_simulaciones
    return probabilidad

# Realizamos simulaciones para diferentes tamaños de grupo
resultados = {}
for n in [5, 10, 15, 20, 23, 30, 40, 50, 60]:
    probabilidad = cumpleaños_simulacion(n)
    resultados[n] = probabilidad

# Imprimir los resultados
for n, probabilidad in resultados.items():
    print(f"Número de personas: {n} -> Probabilidad de coincidencia: {probabilidad:.3f}")
