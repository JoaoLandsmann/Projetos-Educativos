#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

#criando vetores vazios
vetor1 = [] 
vetor2 = []
vetor3 = []

for i in range (10):
    #obtendo os valores para os vetores 1 e 2
    input1 = int(input("Informe o valor do vetor 1: "))
    input2 = int(input("Informe o valor do vetor 2: ")) 

    #adicionando os valores aos respectivos vetores
    vetor1.append(input1)
    vetor2.append(input2)

for j in range(10):
    #inserindo os valores dos vetores 1 e 2 de maneira intercalada no vetor 3
    vetor3.append(vetor1[j])
    vetor3.append(vetor2[j])
    j += 1

#imprimindo o vetor 3 em tela
print(f"O vetor 1 intercalado com o vetor 2 gerou o vetor: {vetor3}")


