import random

def simulacion_enfermedad(num_simulaciones=1000000):
    positivos = 0
    enfermos_positivos = 0

    for _ in range(num_simulaciones):
        # Paso 1: Determinar si la persona tiene la enfermedad (1 de cada 10,000)
        tiene_enfermedad = random.random() < 1/10000  # True si tiene la enfermedad

        # Paso 2: Simular el test
        if tiene_enfermedad:
            test_positivo = random.random() < 0.99  # 99% de probabilidad de dar positivo si tiene la enfermedad
        else:
            test_positivo = random.random() < 0.02  # 2% de probabilidad de dar positivo si no tiene la enfermedad

        # Paso 3: Contar los casos donde el test es positivo
        if test_positivo:
            positivos += 1
            if tiene_enfermedad:
                enfermos_positivos += 1

    # Calcular la probabilidad empírica
    if positivos == 0:
        return 0  # Evitar división por cero
    probabilidad_empirica = enfermos_positivos / positivos
    return probabilidad_empirica

# Ejecutar la simulación
probabilidad_empirica = simulacion_enfermedad()
print(f"Probabilidad empírica de tener la enfermedad dado un test positivo: {probabilidad_empirica:.4f}")

# Parámetros del problema
P_E = 1 / 10000  # Probabilidad de tener la enfermedad
P_noE = 1 - P_E  # Probabilidad de no tener la enfermedad
P_pos_E = 0.99  # Probabilidad de test positivo dado que tiene la enfermedad
P_pos_noE = 0.02  # Probabilidad de test positivo dado que no tiene la enfermedad

# Calcular P(positivo)
P_pos = P_pos_E * P_E + P_pos_noE * P_noE

# Calcular P(E | positivo) usando el teorema de Bayes
P_E_pos = (P_pos_E * P_E) / P_pos

print(f"Probabilidad exacta de tener la enfermedad dado un test positivo: {P_E_pos:.4f}")
