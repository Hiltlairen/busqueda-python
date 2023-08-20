#listas
G=[]
#recordandO PYTHON
#importando 
from grafos import grafos_c
            
def menu ():
    op=1
    grafos=grafos_c()
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