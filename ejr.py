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
    
    def crear_diccionario(self):
        self.crear_lista()
        for i in range(len(self.lista)):
            self.lista_de_dic.append(dict(zip(self.lista[0], self.lista[i])))
        del self.lista_de_dic[0]
        return self.lista_de_dic