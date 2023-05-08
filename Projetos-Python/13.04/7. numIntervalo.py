#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

#obtendo input do usuário
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))

#criando um vetor vazio 
num_intervalo = []

#setando o range como sendo as variáveis
for i in range(int1+1, int2):
    num_intervalo.append(i)

#imprimindo resultado em tela
print(num_intervalo)