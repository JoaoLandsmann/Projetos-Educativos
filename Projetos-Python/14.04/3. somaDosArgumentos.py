#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#obtendo input do usuário
numero1 = float(input("Digite o 1° número: "))
numero2 = float(input("Digite o 2° número: "))
numero3 = float(input("Digite o 3° número: "))

#criando a função de soma
def soma(num1, num2, num3):
    print(num1 + num2 + num3)

#inserindo o input na função
soma(numero1, numero2, numero3)