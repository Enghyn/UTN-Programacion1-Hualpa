#Estudiante: Enzo Giaquinta comisión 4
#Actividades

parcial_1 = int(input("Ingrese la nota del primer parcial: "))
parcial_2 = int(input("Ingrese la nota del segundo parcial: "))
parcial_3 = int(input("Ingrese la nota del tercer parcial: "))

promedio_parciales = (parcial_1 + parcial_2 + parcial_3) / 3

examen_final = int(input("Ingrese la nota del examen final: "))

trabajo_final = int(input("Ingrese la nota del trabajo final: "))

calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print(f"La calificación final del alumno es: {calificacion_final}")
