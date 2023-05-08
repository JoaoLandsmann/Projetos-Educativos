#Faça um Programa que leia três números e mostre o maior e o menor deles.

#obtendo inputs do usuário
numeros = input("Digite três números inteiros separados por espaço ").split(" ")

#convertendo para int
numeros = [int(num) for num in numeros]

#verificando qual o maior e qual o menor número
numero_max = max(numeros)
numero_min = min(numeros)

#imprimindo o resultado 
print(f"O maior número é: {numero_max}")
print(f"O menor número é: {numero_min}")