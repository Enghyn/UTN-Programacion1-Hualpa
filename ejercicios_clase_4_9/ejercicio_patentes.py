while True:
    PATENTE = input("Ingrese patente (formato AAA000): ").upper()
    if len(PATENTE) == 6 and PATENTE[:3].isalpha() and PATENTE[3:].isdigit():
        break
    else:
        print("Patente inválida. Intente nuevamente.")

while True:
    numero_a_ingresar = int(input("Ingrese número a sumar (0-999999): "))
    if 0 <= numero_a_ingresar <= 999999:
        break
    else:
        print("Número inválido. Intente nuevamente.")

ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMERO_MAXIMO = 9

longitud_numero = len(str(numero_a_ingresar))
LONGITUD_PATENTE = 6

digitos = [int(d) for d in str(numero_a_ingresar)]

for i in range(LONGITUD_PATENTE - longitud_numero):
    digitos.insert(0,0)

patente_numero = []
for elemento in PATENTE:
    print(elemento)
    if elemento.isalpha():
        patente_numero.append(ABECEDARIO.index(elemento))
    else:
        patente_numero.append(int(elemento))


fuera_de_rango = False
for i in range(len(patente_numero) - 1, -1, -1):
    patente_numero[i] += digitos[i]
    if i >= 3:
        if patente_numero[i] > NUMERO_MAXIMO:
            patente_numero[i] -= NUMERO_MAXIMO + 1
            patente_numero[i - 1] += 1
    elif 3 > i > 0:
        if patente_numero[i] > len(ABECEDARIO):
            patente_numero[i] -= len(ABECEDARIO)
            patente_numero[i - 1] += 1
    else:
        if patente_numero[i] >= len(ABECEDARIO):
            print("Patente fuera de rango")
            fuera_de_rango = True

if not fuera_de_rango:
    nueva_patente = ""
    for i in range(len(patente_numero)):
        if i <= 3:
            nueva_patente += ABECEDARIO[patente_numero[i]]
        else:
            nueva_patente += str(patente_numero[i])
    print(f"Nueva patente: {nueva_patente}")
