def hanoi(n,origem,destino,trabalho):
    if (n > 0):
        hanoi(n - 1, origem, trabalho, destino)
        mover(origem, destino)
        hanoi(n - 1, trabalho, destino, origem)
	
def mover(origem,destino):
    print("De",origem,"para",destino)
    
hanoi(4,"A","C","B")
	

        