#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

#obtendo input do usuário
num = int(input("Digite um número inteiro: "))

#verificando se é positivo ou negativo e imprimindo o resultado
if num > 0:
    print(f"O número ({num}) é positivo!")
else:
    print(f"O número ({num}) é negativo!")