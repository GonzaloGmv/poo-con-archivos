class calificaciones:
    def __init__(self):
        f = open('calificaciones.csv', 'r', encoding="utf-8")
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
        alumno2 = []
        alumno3 = []
        alumno4 = []
        alumno5 = []
        alumno6 = []
        alumno7 = []
        alumno8 = []
        alumno9 = []
        alumno10 = []
        alumno11 = []
        alumno12 = []
        alumno13 = []
        alumno14 = []
        alumno15 = []
        alumno16 = []
        self.apellidos = apellidos
        self.nombre = nombre
        self.asistencia = asistencia
        self.Parcial1 = Parcial1
        self.Parcial2 = Parcial2
        self.Ordinario1 = Ordinario1
        self.Ordinario2 = Ordinario2
        self.Practicas = Practicas
        self.OrdinarioPracticas = OrdinarioPracticas
        self.f = f
        self.alumno1 = alumno1
        self.alumno2 = alumno2
        self.alumno3 = alumno3
        self.alumno4 = alumno4
        self.alumno5 = alumno5
        self.alumno6 = alumno6
        self.alumno7 = alumno7
        self.alumno8 = alumno8
        self.alumno9 = alumno9
        self.alumno10 = alumno10
        self.alumno11 = alumno11
        self.alumno12 = alumno12
        self.alumno13 = alumno13
        self.alumno14 = alumno14
        self.alumno15 = alumno15
        self.alumno16 = alumno16
    
    def separar(self):
        next(self.f)
        for i in self.f:
            i = i.rstrip('\n')
            columnas = i.split(';')
            self.apellidos.append(columnas[0])
            self.nombre.append(columnas[1])
            self.asistencia.append(columnas[2])
            self.Parcial1.append(columnas[3])
            self.Parcial2.append(columnas[4])
            self.Ordinario1.append(columnas[5])
            self.Ordinario2.append(columnas[6])
            self.Practicas.append(columnas[7])
            self.OrdinarioPracticas.append(columnas[8])
    
    def alumno(alumno, num_alumno, self):
        self.separar()
        alumno.append(self.apellidos[num_alumno])
        alumno.append(self.nombre[num_alumno])
        alumno.append(self.asistencia[num_alumno])
        alumno.append(self.Parcial1[num_alumno])
        alumno.append(self.Parcial2[num_alumno])
        alumno.append(self.Ordinario1[num_alumno])
        alumno.append(self.Ordinario2[num_alumno])
        alumno.append(self.Practicas[num_alumno])
        alumno.append(self.OrdinarioPracticas[num_alumno])
        return alumno
    
    def crear(self):
        self.alumno1 = self.alumno(self.alumno1, 0)
        self.alumno2 = self.alumno(self.alumno2, 1)
        self.alumno3 = self.alumno(self.alumno3, 2)
        self.alumno4 = self.alumno(self.alumno4, 3)
        self.alumno5 = self.alumno(self.alumno5, 4)
        self.alumno6 = self.alumno(self.alumno6, 5)
        self.alumno7 = self.alumno(self.alumno7, 6)
        self.alumno8 = self.alumno(self.alumno8, 7)
        self.alumno9 = self.alumno(self.alumno9, 8)
        self.alumno10 = self.alumno(self.alumno10, 9)
        self.alumno11 = self.alumno(self.alumno11, 10)
        self.alumno12 = self.alumno(self.alumno12, 11)
        self.alumno13 = self.alumno(self.alumno13, 12)
        self.alumno14 = self.alumno(self.alumno14, 13)
        self.alumno15 = self.alumno(self.alumno15, 14)
        self.alumno16 = self.alumno(self.alumno16, 15)

ejer = calificaciones()
ejer.crear()