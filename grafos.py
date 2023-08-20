from operaciones import operaciones

class grafos_c:
    def __init__(self):
        self.opg=operaciones
        self.GN={}
    def crando(self):
        nodo=input("nombre del nodo:")
        self.GN=dict(nodo)
        a=len(self.GN)
        if nodo not in self.GN:
            self.GN[nodo] = []
    def ver_nodos(self):
        for i in range (len(self.GN)):
            print((i+1),".-",self.GN[i]) 
    def conexiones(self):
        #buscar el grafo
        nomG=input("ingrese el grafo a conectar:")
        self.opg.buscar(nomG,self.GN)
        #asignando conexiones
        for i in range (len(self.GN)):
            cg=str(input("conexiones:"))
            self.GN[i]=cg
        print(self.GN)
        