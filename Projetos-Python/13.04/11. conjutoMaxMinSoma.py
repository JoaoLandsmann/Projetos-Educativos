#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

#obtendo input do usuário com a lista desejada
conjunto_N = input("Digite um conjunto de números separados por espaço: ").split(" ")

#convertendo essa lista para float e armazenando no vetor conjunto_N
conjunto_N = [float(num) for num in conjunto_N]

#verificando o maior, menor e realizando a soma. Imprimindo em tela
print(f"O maior número dessa lista é: {max(conjunto_N)}")
print(f"O menor número dessa lista é: {min(conjunto_N)}")
print(f"A soma dos números dessa lista é: {sum(conjunto_N):.2f}")

