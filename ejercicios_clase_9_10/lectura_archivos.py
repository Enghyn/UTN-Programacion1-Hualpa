RUTA = "./ejercicios_clase_9_10/listaAlumnosC4.txt"

with open(RUTA, "r", encoding="utf-8") as archivo:
    alumnos = archivo.read().split(";")
    alumnos = sorted(alumnos)
    for alumno in alumnos:
        print(alumno)