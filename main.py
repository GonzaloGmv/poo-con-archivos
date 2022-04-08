from clases.ejr import *

if __name__ == '__main__':
    ejr = calificaciones()
    print("Estos son todos los alumnos")
    print(ejr.diccionario_alumnos(), '\n')
    print("Aprobados:")
    print(ejr.diccionario_aprobados(), '\n')
    print("Suspensos:")
    print(ejr.diccionario_suspensos())