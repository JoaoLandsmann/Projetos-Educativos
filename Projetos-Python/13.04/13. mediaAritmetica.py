#Faça um programa que calcule o mostre a média aritmética de N notas.

#obtendo input do usuário
notas = input("Digite todas as notas separadas por espaço: ").split(" ")

#convertendo para float e armazenando no vetor notas
notas = [float(nota) for nota in notas]

#somando todos os elementos do vetor
soma = 0
for nota in notas:
    soma += nota

#calculando a média
media_aritmetica = soma / len(notas)

#imprimindo o resultado em tela
print(f"A média entre as notas inseridas é: {media_aritmetica:.2f}")