#sudoku
def Validar_Linhas(Ma):
    colunas = []
    for i in range(9):
        pd_coluna = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for j in range(0,17,2):
            procede = False
            for k in pd_coluna.keys():
                if k == Ma[i][j]:
                    pd_coluna[Ma[i][j]] += 1
                    procede = True
            if not procede:
                return False
        colunas.append(pd_coluna.values())
    for i in range(len(colunas)):
        for j in colunas[i]:
            if j != 1:
                return False
    return True
def Validar_Colunas( Mat ):
    linhas = []
    for h in range(0, 17, 2):
        pd_linha = {'1':0,'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0 }
        for j in range(9):
            procede = False
            for k in pd_linha.keys():
                if k == Mat[j][h]:
                    pd_linha[Mat[j][h]] += 1
                    procede = True
            if not procede:
                return False
        linhas.append(pd_linha.values())
    for o in range(len(linhas)):
        for j in linhas[o]:
            if j != 1:
                return False
    return True
def Validar_jogo3x3(M):
    padrao = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    A = [0,3,6]
    B = [0,6,12]
    M3x3 = []
    for i in A:
        ifi = i+3
        for j in B:
            jf = j + 5
            padrao = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for i1 in range(i,ifi):
                for j1 in range(j,jf,2):
                    #print(range(j,jf,2), M[i1][j1])
                    procede = False
                    for y in padrao.keys():
                        if y == M[i1][j1]:
                            padrao[M[i1][j1]]+=1
                            procede = True
                    if not procede:
                        return False
            M3x3.append(padrao.values())
    for i in range(len(M3x3)):
        for j in M3x3[i]:
            if j != 1:
                return False
    return True
jogada_sudoku=[]
for i in range(9):
    jogada_sudoku.append(input())
print(Validar_jogo3x3(jogada_sudoku) and Validar_Colunas(jogada_sudoku) and Validar_Linhas(jogada_sudoku) )


