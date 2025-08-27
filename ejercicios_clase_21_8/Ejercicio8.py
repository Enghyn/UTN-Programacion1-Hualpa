#Estudiante: Enzo Giaquinta comisión 4
#Actividades

VELOCIDAD_PROMEDIO = 90
LITROS_POR_KM = 8 / 100

distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
precio_gasolina = float(input("Ingrese el precio de la gasolina por litro: "))

litros_necesarios = distancia * LITROS_POR_KM
costo_viaje = litros_necesarios * precio_gasolina
horas_viaje = distancia / VELOCIDAD_PROMEDIO

print(f"El viaje tomará {horas_viaje} horas y costará ${costo_viaje} en gasolina. Se necesitarán {litros_necesarios} litros de gasolina.")