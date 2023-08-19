#listas
G=[]
#recordandO PYTHON
class busqueda:
    def __init__(self):
        self.GN=[]
    def crando(self):
        ng=str(input("nombre del nodo:"))
        self.GN.append(ng)
    def ver_nodos(self):
        for i in range (len(self.GN)):
            print((i+1),".-",self.GN[i]) 
            
def menu ():
    op=1
    grafos=busqueda()
    while(op!=9):
        print("MENU")
        print("1.- Añadir los grafos")
        print("2.- Ver grafos")
        print("9.- Salir")
        op=int(input(":"))
        if op==1:
            grafos.crando()
        elif op==2:
            grafos.ver_nodos()

menu()
