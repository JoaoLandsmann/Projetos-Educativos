#escrevendo um nome em uma escada invertida

#obtendo input do usuário
nome = input("Qual o seu nome?")

#montando a escada invertida
for i in range(0,len(nome)):
    print(nome[i:])