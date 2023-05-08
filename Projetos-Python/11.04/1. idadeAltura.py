#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

#criando os vetores vazios
idade_vetor = []
altura_vetor = []

for i in range (5):
    #obtendo idade e altura de cada pessoa
    idade = int(input(f"Digite a idade da pessoa {i+1} : "))
    altura = float(input(f"Digite a altura da pessoa {i+1} :"))

    #adicionando ao respectivo vetor
    idade_vetor.append(idade)
    altura_vetor.append(altura)
    i += 1 

#exibindo resultado em tela
print(f"A idade invertida das pessoas, em metros, é de : {idade_vetor[::-1]}")
print(f"A altura invertida das pessoas, em metros, é de : {altura_vetor[::-1]}")
