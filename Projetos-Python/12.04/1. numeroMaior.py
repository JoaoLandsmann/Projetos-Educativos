#Faça um Programa que peça dois números e imprima o maior deles.

#pegando input do usuário
num1 = int(input(("Digite o 1° número")))
num2 = int(input(("Digite o 2° número")))
           
#comparando os números e imprimindo o resultado
if num1 > num2:
    print(f"O primeiro número é o primeiro ({num1})!")
else:
    print(f"O maior número é o segundo ({num2})!")

    