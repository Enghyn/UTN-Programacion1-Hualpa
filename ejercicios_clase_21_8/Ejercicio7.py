#Estudiante: Enzo Giaquinta comisión 4
#Actividades

dolares = float(input("Ingrese la cantidad de dólares a convertir: "))

DIVISA_COLOMBIANA = 3987
DIVISA_ARGENTINA = 1301
DIVISA_EURO = 0.85

pesos_colombianos = dolares * DIVISA_COLOMBIANA
pesos_argentinos = dolares * DIVISA_ARGENTINA
euros = dolares * DIVISA_EURO

print(f"${dolares} dólares son {pesos_colombianos} pesos colombianos.")
print(f"${dolares} dólares son {pesos_argentinos} pesos argentinos.")
print(f"${dolares} dólares son {euros} euros.")