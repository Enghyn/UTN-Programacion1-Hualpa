#Estudiante: Enzo Giaquinta comisión 4
#Actividades

monto_solicitado = int(input("Ingrese el monto a calcular: "))
CANTIDAD_MESES = 12
PORCENTAJE_INTERES = 2

monto_total = monto_solicitado * (1 + (PORCENTAJE_INTERES / 100))**CANTIDAD_MESES
monto_por_mes = monto_total / CANTIDAD_MESES

print(f"Monto total: {monto_total}")
print(f"Monto por mes: {monto_por_mes}")