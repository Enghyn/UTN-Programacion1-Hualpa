#Estudiante: Enzo Giaquinta comisión 4
#Actividades

#Ejercicio pizarra
es_Veraz = ""
while es_Veraz != "si":
    es_Veraz = input("¿Está en el Veraz? (si/no): ").lower()
    if es_Veraz == "no":
        print("No puede solicitar un préstamo si está en el Veraz.")
        exit()
    elif es_Veraz != "si":
        print("Respuesta no válida.")
        continue

while True:
    print("""Puede solicitar un préstamo.
          
          1) Solicitar préstamo.
          2) Salir.""")
    opcion = input("Seleccione una opción: ")
    if opcion == "2":
        print("Saliendo...")
        break
    elif opcion != "1":
        print("Opción no válida.")
        continue

    monto_solicitado = 0
    while monto_solicitado <= 0:
        monto_solicitado = int(input("Ingrese el monto del préstamo: "))
        if monto_solicitado <= 0:
            print("El monto solicitado debe ser mayor a 0.")
    
    cantidad_meses = 0
    while 12 > cantidad_meses > 72:
        cantidad_meses = int(input("Ingrese la cantidad de meses a pagar el préstamo: "))
        if 12 > cantidad_meses > 72:
            print("La cantidad de meses debe estar entre 12 y 72.")
    
    porcentaje_interes = 0
    while porcentaje_interes <= 0:
        porcentaje_interes = int(input("Ingrese el porcentaje de interés: "))
        if porcentaje_interes <= 0:
            print("El porcentaje de interés debe ser mayor a 0.")

    monto_total = monto_solicitado * (1 + (porcentaje_interes / 100))**cantidad_meses
    cuota_mensual = monto_total / cantidad_meses
    print(f"Monto total a pagar (incluido los intereses): {monto_total}")
    print(f"Cuota mensual: {cuota_mensual}")

    ingresos_netos_mensuales = 0
    while ingresos_netos_mensuales <= 0:
        ingresos_netos_mensuales = float(input("Ingrese sus ingresos netos mensuales: "))
        if ingresos_netos_mensuales <= 0:
            print("Los ingresos netos mensuales deben ser mayores a 0.")
        
        elif (ingresos_netos_mensuales * 0.30) < cuota_mensual:
            print(f"No puede solicitar el préstamo, la cuota mensual ({cuota_mensual}) excede el 30% de sus ingresos netos mensuales ({ingresos_netos_mensuales}).")
            exit()

    print("Préstamo aprobado.")