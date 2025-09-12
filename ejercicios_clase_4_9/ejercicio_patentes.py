while True:
    PATENTE = input("Ingrese patente (formato AAA000): ").upper()
    if len(PATENTE) == 6 and PATENTE[:3].isalpha() and PATENTE[3:].isdigit():
        break
    else:
        print("Patente inválida. Intente nuevamente.")

while True:
    numero_a_ingresar = int(input("Ingrese número a sumar a la patente: "))
    if 0 <= numero_a_ingresar < 17576000:
        break
    else:
        print("Número inválido o fuera del rango posible. Intente nuevamente.")

ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMERO_MAXIMO = 999

patente_numero = []
for elemento in PATENTE:
    if elemento.isalpha():
        patente_numero.append(ABECEDARIO.index(elemento))
    else:
        patente_numero.append(int(PATENTE[3:]))
        break

if numero_a_ingresar > 676000:
    patente_numero[0] += numero_a_ingresar // 676000
    numero_a_ingresar = numero_a_ingresar % 676000
if numero_a_ingresar > 26000:
    patente_numero[1] += numero_a_ingresar // 26000
    numero_a_ingresar = numero_a_ingresar % 26000
if numero_a_ingresar > 1000:
    patente_numero[2] += numero_a_ingresar // 1000
    numero_a_ingresar = numero_a_ingresar % 1000
if numero_a_ingresar > 0:
    patente_numero[3] += numero_a_ingresar

LONGITUD_PATENTE = len(patente_numero)

for i in range(LONGITUD_PATENTE - 1, -1, -1):
    if i == 3 and patente_numero[i] > NUMERO_MAXIMO:
        patente_numero[i] -= NUMERO_MAXIMO + 1
        patente_numero[i - 1] += 1
    elif 3 > i > 0 and patente_numero[i] >= len(ABECEDARIO):
        patente_numero[i] -= len(ABECEDARIO)
        patente_numero[i - 1] += 1
    elif i == 0 and patente_numero[i] >= len(ABECEDARIO):
        print("Patente fuera de rango")
        exit()

nueva_patente = ""
for i in range(LONGITUD_PATENTE):
    if i < 3:
        nueva_patente += ABECEDARIO[patente_numero[i]]
    else:
        if patente_numero[i] < 10:
            nueva_patente += "00" + str(patente_numero[i])
        elif 10 <= patente_numero[i] < 100:
            nueva_patente += "0" + str(patente_numero[i])
        else:
            nueva_patente += str(patente_numero[i])
print(f"Nueva patente: {nueva_patente}")
