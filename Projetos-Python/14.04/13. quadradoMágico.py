#Quadrado mágico. 
#Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
#Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
#8  3  4 
#1  5  9
#6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
#Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

import random
                                                   #j(coluna)
matriz = [[1, 2, 3],                        #00 01 02 #\i(linha) 
          [4, 5, 6],                        #10 11 12
          [7, 8, 9]]                        #20 21 22
          
resultado = False

# definindo uma função para validar se a matriz é um quadrado mágico
def quadrado_magico():
    global resultado

    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        resultado = True
    else:
        # a primeira vez vai cair no false porque a primeira matriz não é um quadrado mágico
        resultado = False
    return resultado
 
# loop para repetir a geração de números e a validação até formar um quadrado mágico
while resultado == False:
    for b in range(4):
        for a in range(3):
            vetor_sequencia = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(3):
                for j in range(3):
                    # pegando números aleatórios da sequência
                    z = random.choice(vetor_sequencia)
                    matriz[i][j] = z
                    x = vetor_sequencia.index(z)
                    vetor_sequencia = vetor_sequencia[:x] + vetor_sequencia[x+1:]
            # chama a função para fazer a validação
            resultado = False
            quadrado_magico()

        resultado = resultado
        if resultado == True:
            # imprimindo o quadrado mágico em tela
            print(f"O quadrado mágico é: \n")
            print (matriz[0][0], matriz[0][1], matriz[0][2])
            print (matriz[1][0], matriz[1][1], matriz[1][2])
            print (matriz[2][0], matriz[2][1], matriz[2][2])
        