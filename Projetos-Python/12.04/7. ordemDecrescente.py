#Faça um Programa que leia três números e mostre-os em ordem decrescente.

#obtendo input do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Ordenando os números em ordem decrescente
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

# Imprimindo os números em ordem decrescente
print(num3, num2, num1)