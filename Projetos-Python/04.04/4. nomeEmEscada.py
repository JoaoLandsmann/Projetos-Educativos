#escrevendo um nome em escada

#obtendo input do usuário
nome = input("Qual o seu nome?")

#montando a escada
for i in range(0,len(nome)+1):
    print(nome[:i])