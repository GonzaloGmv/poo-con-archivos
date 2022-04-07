class calificaciones:
    def __init__(self):
        f = open('calificaciones.csv', 'r', encoding="utf-8")
        lista = []
        lista_de_dic = []
        self.f = f
        self.lista = lista
        self.lista_de_dic = lista_de_dic
    
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

    def crear_diccionario(self):
        self.nota_final()
        for i in range(len(self.lista)):
            self.lista_de_dic.append(dict(zip(self.lista[0], self.lista[i])))
        del self.lista_de_dic[0]
        return self.lista_de_dic
    
    def imprimir(self):
        self.crear_diccionario()
        for i in range(len(self.lista_de_dic)):
            print(self.lista_de_dic[i])

        

ejr = calificaciones()
ejr.imprimir()