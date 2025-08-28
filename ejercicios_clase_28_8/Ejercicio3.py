#Estudiante: Enzo Giaquinta comisión 4
#Actividades

print("Bienvenido al sistema de créditos personales")
cliente = input("Por favor, ingrese su nombre y apellido: ")

#Entrada y Validación del CUIT
cuit = input("Por favor, ingrese su CUIT (ej: 20-12345678-9): ")

while True:
    if len(cuit) != 13 or cuit[2] != '-' or cuit[11] != '-' or not (cuit.replace('-', '').isdigit()):
        print("CUIT inválido. Asegúrese de que tenga el formato correcto (ej: 20-12345678-9).")
        cuit = input("Por favor, ingrese su CUIT (ej: 20-12345678-9): ")
    else:
        break

# Entrada y Validación de Ingresos
ingresos_mensuales = float(input("Por favor, ingrese sus ingresos mensuales en pesos: "))
INGRESOS_MINIMOS = 200000
if ingresos_mensuales < INGRESOS_MINIMOS:
    print("Lo sentimos, no es elegible para un crédito debido a sus ingresos mensuales.")
    exit()

# Entrada y Validación de Antigüedad Laboral
antiguedad_laboral = int(input("Por favor, ingrese su antigüedad laboral en años: "))
if antiguedad_laboral < 1:
    print("Lo sentimos, no es elegible para un crédito debido a su antigüedad laboral.")
    exit()

#Seteo, Entrada y Validación de Historial Crediticio
HISTORIAL = {1: "Bueno", 2: "Regular", 3: "Malo"}
historial_crediticio = int(input("Por favor, ingrese su historial crediticio (1-Bueno | 2-Regular | 3-Malo): "))

while True:
    if historial_crediticio not in HISTORIAL:
        print("Historial crediticio inválido. Por favor, ingrese un valor entre 1 y 3.")
        historial_crediticio = int(input("Por favor, ingrese su historial crediticio (1-Bueno | 2-Regular | 3-Malo): "))
    else:
        break

if HISTORIAL[historial_crediticio] == "Malo":
    print("Lo sentimos, no es elegible para un crédito debido a su historial crediticio.")
    exit()

historial_crediticio = HISTORIAL[historial_crediticio]

# Cálculo del monto aprobado
if antiguedad_laboral < 2:
    monto_aprobado = 500000
elif antiguedad_laboral >= 2:
    monto_aprobado = 1000000 if historial_crediticio == HISTORIAL[2] else 3000000

#Salida por consola
print("----------------------\n")
print(f"Cliente: {cliente}")
print(f"CUIT: {cuit}")
print(f"Ingresos: ${ingresos_mensuales}")
print(f"Antigüedad: {antiguedad_laboral} años")
print(f"Historial: {historial_crediticio}")
print(f"Monto aprobado: ${monto_aprobado}")