#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

#setando um valor inicial para a variavel nota_valida
nota_valida = False

#colocando o número de tentativas em 5
for i in range(5):
    #obtendo input do usuário
    nota = int(input("Digite uma nota entre 0 e 10: "))

    #verificando se a nota está entre 0 e 10
    if nota >= 0 and nota <= 10:
        print(f"Nota digitada: {nota}")
        nota_valida = True
        break
    else:
        print("Valor inválido! Digite uma nota entre 0 e 10.")

#caso o usuário exceda o limite de tentativas
if not nota_valida:
    print("Você excedeu o limite de tentativas permitido.")