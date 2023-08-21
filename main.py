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

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        print(inicio, end=" ")

        for vecino in self.grafo[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def bfs(self, inicio):
        visitados = set()
        cola = [inicio]

        while cola:
            nodo_actual = cola.pop(0)
            if nodo_actual not in visitados:
                print(nodo_actual, end=" ")
                visitados.add(nodo_actual)
                cola.extend(vecino for vecino in self.grafo[nodo_actual] if vecino not in visitados)

def mostrar_menu():
    print("1. Crear nodo")
    print("2. Enlazar nodos")
    print("3. Mostrar grafo")
    print("4. Búsqueda en Profundidad (DFS)")
    print("5. Búsqueda en Amplitud (BFS)")
    print("6. Salir")

mi_grafo = Grafo()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nodo = input("Ingrese el nombre del nodo: ")
        mi_grafo.agregar_nodo(nodo)
        print("Nodo", nodo, "creado.")
    elif opcion == '2':
        nodo1 = input("Ingrese el nombre del primer nodo: ")
        nodo2 = input("Ingrese el nombre del segundo nodo: ")
        mi_grafo.agregar_arista(nodo1, nodo2)
        print("Enlace creado entre", nodo1, "y", nodo2)
    elif opcion == '3':
        mi_grafo.mostrar_grafo()
    elif opcion == '4':
        nodo_inicio = input("Ingrese el nodo de inicio para DFS: ")
        print("Búsqueda en Profundidad (DFS):")
        mi_grafo.dfs(nodo_inicio)
    elif opcion == '5':
        nodo_inicio = input("Ingrese el nodo de inicio para BFS: ")
        print("Búsqueda en Amplitud (BFS):")
        mi_grafo.bfs(nodo_inicio)
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
