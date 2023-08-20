class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)

    def mostrar_grafo(self):
        for nodo, vecinos in self.grafo.items():
            print(nodo, "->", vecinos)
        