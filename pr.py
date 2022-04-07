f = open('calificaciones.csv', 'r', encoding="utf-8")
next(f)
apellidos = []
nombre = []
asistencia = []
Parcial1 = []
Parcial2 = []
Ordinario1 = []
Ordinario2 = []
Practicas = []
OrdinarioPracticas = []
alumno1 = []

for i in f:
    i = i.rstrip('\n')
    columnas = i.split(';')
    apellidos.append(columnas[0])
    nombre.append(columnas[1])
    asistencia.append(columnas[2])
    Parcial1.append(columnas[3])
    Parcial2.append(columnas[4])
    Ordinario1.append(columnas[5])
    Ordinario2.append(columnas[6])
    Practicas.append(columnas[7])
    OrdinarioPracticas.append(columnas[8])

print(apellidos)
print(nombre)
print(asistencia)
print(Parcial1)
print(Parcial2)
print(Ordinario1)
print(Ordinario2)
print(OrdinarioPracticas)

for i in f:
    alumno1 = i

print(alumno1)