#Altere o programa anterior para mostrar no final a soma dos números.

#obtendo input do usuário
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))

#criando um vetor vazio 
num_intervalo = []

#setando o range como sendo as variáveis
for i in range(int1+1, int2):
    num_intervalo.append(i)

#imprimindo resultado em tela
print(f"A soma dos números no intervalo entre {int1} e {int2} é {sum(num_intervalo)}")