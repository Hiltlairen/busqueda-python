class grafos_c:
    def __init__(self):
        self.GN=[]
    def crando(self):
        ng=str(input("nombre del nodo:"))
        self.GN.append(ng)
    def ver_nodos(self):
        for i in range (len(self.GN)):
            print((i+1),".-",self.GN[i]) 