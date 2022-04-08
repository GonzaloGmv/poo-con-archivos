# poo-con-archivos

El link a este repositorio es: [ github](https://github.com/GonzaloGmv/poo-con-archivos)

El código de este ejercicio es el siguiente:
```
class calificaciones:
    def __init__(self):
        f = open('calificaciones.csv', 'r', encoding="utf-8")
        lista = []
        lista_de_dic = []
        aprobados = []
        suspensos = []
        dic_aprobados = []
        dic_suspensos = []
        self.f = f
        self.lista = lista
        self.lista_de_dic = lista_de_dic
        self.aprobados = aprobados
        self.suspensos = suspensos
        self.dic_aprobados = dic_aprobados
        self.dic_suspensos = dic_suspensos
    
    def crear_lista(self):
        for i in self.f:
            i = i.rstrip('\n')
            columnas = i.split(';')
            self.lista.append(columnas)
        return self.lista
    
    def mejorar(self):
        self.crear_lista()
        for i in range(len(self.lista)):
            for j in range(len(self.lista[i])):
                if self.lista[i][j] == '':
                    self.lista[i][j] = 0
        self.lista[0].append('Nota final')
        return self.lista
    
    def nota_final(self):
        self.mejorar()
        for i in range(1, len(self.lista)):
            nota = 0.3 * float(self.lista[i][3]) +  0.3 * float(self.lista[i][4]) +  0.4 * float(self.lista[i][7])
            self.lista[i].append(nota)
        return self.lista

    def aprobado(self):
        for i in range(1, len(self.lista)):
            if self.lista[i][2] >= '75%' and float(self.lista[i][3]) >= 4 and float(self.lista[i][4]) >= 4 and float(self.lista[i][7]) >= 4 and float(self.lista[i][9]) >= 5:
                self.aprobados.append(self.lista[i])
            else:
                self.suspensos.append(self.lista[i])
        return self.aprobados, self.suspensos

    def diccionario_alumnos(self):
        self.nota_final()
        for i in range(len(self.lista)):
            self.lista_de_dic.append(dict(zip(self.lista[0], self.lista[i])))
        del self.lista_de_dic[0]
        return self.lista_de_dic
    
    def diccionario_aprobados(self):
        self.aprobado()
        for i in range(len(self.aprobados)):
            self.dic_aprobados.append(dict(zip(self.lista[0], self.aprobados[i])))
        return self.dic_aprobados

    def diccionario_suspensos(self):
        for i in range(len(self.suspensos)):
            self.dic_suspensos.append(dict(zip(self.lista[0], self.suspensos[i])))
        return self.dic_suspensos
```

El main de este ejercicio es el siguiente:
```
from clases.ejr import *

if __name__ == '__main__':
    ejr = calificaciones()
    print("Estos son todos los alumnos")
    print(ejr.diccionario_alumnos(), '\n')
    print("Aprobados:")
    print(ejr.diccionario_aprobados(), '\n')
    print("Suspensos:")
    print(ejr.diccionario_suspensos())
```    
