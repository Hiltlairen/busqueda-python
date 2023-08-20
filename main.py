from grafos import Grafo

def mostrar_menu():
    print("1. Crear nodo")
    print("2. Enlazar nodos")
    print("3. Mostrar grafo")
    print("4. Salir")

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
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")