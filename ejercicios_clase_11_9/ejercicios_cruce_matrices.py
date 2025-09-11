import random

matriz_binario = []

TAMAÑO_MATRIZ = 5
contador_barcos = 0
for fila in range(TAMAÑO_MATRIZ):
    matriz_binario.append([])
    for columna in range(TAMAÑO_MATRIZ):
        valor = random.randint(0, 1)
        matriz_binario[fila].append(valor)
        if valor == 1:
            contador_barcos += 1

matriz_usuario = []
for fila in range(TAMAÑO_MATRIZ):
    matriz_usuario.append([])
    for columna in range(TAMAÑO_MATRIZ):
        matriz_usuario[fila].append("-")

while True:
    print("    0    1    2    3    4  C")
    for fila in range(TAMAÑO_MATRIZ):
        print(f"{fila} {matriz_usuario[fila]}")
        if fila == TAMAÑO_MATRIZ - 1:
            print("F")

    while True:
        fila_usuario = int(input(f"Ingrese fila (0 a {TAMAÑO_MATRIZ - 1}): "))
        columna_usuario = int(input(f"Ingrese columna (0 a {TAMAÑO_MATRIZ - 1}): "))
        if 0 <= fila_usuario < TAMAÑO_MATRIZ and 0 <= columna_usuario < TAMAÑO_MATRIZ:
            break
        else:
            print("\nCoordenadas fuera de rango. Intente de nuevo.")

    posicion_usuario = matriz_binario[fila_usuario][columna_usuario]
    
    if posicion_usuario == 1:
        matriz_usuario[fila_usuario][columna_usuario] = "X"
        matriz_binario[fila_usuario][columna_usuario] = "-"
        print("\n¡Acertaste! Has hundido un barco.")
        contador_barcos -= 1
    elif posicion_usuario == 0:
        matriz_usuario[fila_usuario][columna_usuario] = "O"
        print("\n¡Fallaste!")
    else:
        print("\nYa has intentado esa posición. Intenta de nuevo.")
        continue

    if contador_barcos == 0:
        print("\n¡Felicidades! Has hundido todos los barcos.")
        break