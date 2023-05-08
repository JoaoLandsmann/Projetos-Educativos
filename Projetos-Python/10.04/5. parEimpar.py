#lendo os números inteiros, armazenando-os em um vetor e separando os pares de ímpares

#criando vetores vazios
vetor1 = []   #geral
vetor2 = []   #pares
vetor3 = []   #impares

#obtendo input do usuário e inserindo no vetor1
for i in range(5):
    number = int(input("Digite um número"))
    vetor1.append(number)

    #verificando se o número é par ou ímpar e inserindo no respectivo vetor
    if (number % 2) == 0:
        vetor2.append(number)
    else:
        vetor3.append(number)

#imprimindo resultado em tela
print(vetor1)
print(vetor2)
print(vetor3)