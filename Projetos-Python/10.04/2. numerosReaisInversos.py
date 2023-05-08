#lendo um vetor com 5 números reais e mostrando eles na ordem inversa

#criando vetor vazio
vetor = []

#obtendo input do usuário e inserindo no vetor
for i in range(5):
    num = float(input("Digite um número inteiro: "))
    vetor.append(num)

#invertendo a ordem do vetor
vetor.reverse()

#imprimindo o resultado em tela
print(f"O vetor na ordem inversa é: {vetor}")